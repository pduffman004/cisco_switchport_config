from getpass import getpass
import json

from napalm import get_network_driver
from ciscoconfparse import CiscoConfParse
from jinja2 import Environment, FileSystemLoader


# AD credentials and enable password to connect to switch.
username = input('AD username: ')
password = getpass('Password: ')
enable_pwd = getpass('Enable pwd: ')

# Read switch information from json file.
with open('switch_info.json') as f_obj:
    config_data = f_obj.read()
    config_dict = json.loads(config_data)

# Iterate over floors/IDFs listed in json file to gather current & new vlans.
for floor in range(len(config_dict["floors"])):
    current_user_vlan = config_dict["floors"][floor]["current_user_vlan"]
    current_voice_vlan = config_dict["floors"][floor]["current_voice_vlan"]
    current_video_vlan = config_dict["floors"][floor]["current_video_vlan"]
    new_user_vlan = config_dict["floors"][floor]["new_user_vlan"]
    new_voice_vlan = config_dict["floors"][floor]["new_voice_vlan"]
    new_video_vlan = config_dict["floors"][floor]["new_video_vlan"]

    # Iterate over switches in floor/IDF to gather hostname, IP.
    for switch in config_dict["floors"][floor]["switches"]:
        mgmt_ip = switch['mgmt_ip']
        hostname = switch['hostname']

        print(f'Connecting to {hostname}...')
        # Create connection to switch, collect run config.
        with get_network_driver('ios')(
                mgmt_ip,
                username,
                password,
                optional_args={
                    'secret': enable_pwd,
                    'inline_transfer': True,
                    'global_delay_factor': 2,
                    }
                ) as device:
            config = device.get_config()

            # Write current config to local machine as text file.
            print('Writing current config file to local machine...')
            with open(f'{hostname}_currentconfig.txt', 'w') as s_f_obj:
                s_f_obj.write(config['running'])

            # Create ConfParse object, find interfaces.
            config_obj = CiscoConfParse(config=config['running'].split('\n'))
            interface_cnfgs = config_obj.find_objects(r'^interface')

            # Create list of access interfaces.
            interfaces_to_change = []
            for interface in interface_cnfgs:
                if interface.re_search_children(
                        f'^ switchport access vlan {current_user_vlan}$'
                        ):
                    interfaces_to_change.append(
                        {'name': interface.text, 'type': 'user'}
                        )
                elif interface.re_search_children(
                        f'^ switchport access vlan {current_video_vlan}$'
                        ):
                    interfaces_to_change.append(
                        {'name': interface.text, 'type': 'video'}
                        )

            # Jinja template creates config changes.
            ENV = Environment(
                loader=FileSystemLoader('.'),
                trim_blocks=True,
                lstrip_blocks=True,
                keep_trailing_newline=True,
                )
            config = ENV.get_template('conf_template.j2')
            config_text = config.render(interface_list=interfaces_to_change,
                                        voice_vlan=new_voice_vlan,
                                        users_vlan=new_user_vlan,
                                        video_vlan=new_video_vlan,
                                        )
            # Print config changes that will be sent to switch.
            print('The following commands will be sent to script (loading):')
            print(config_text)
            # Print napalm net changes.
            print('Loading net changes (this may take a few minutes)...')
            device.load_merge_candidate(config=config_text)
            print(device.compare_config())

            # Ask for confirmation to commit changes.
            response = ''
            while response not in ('y', 'n'):
                response = input("Commit the above changes? (y/n): ")
                if response == 'n':
                    device.discard_config()
                    print('Changes discarded, moving on to next device, '
                          'press ctrl+c to cancel.')
                if response == 'y':
                    device.commit_config()
                    print('Changes committed.')
