

# Cisco Switchport Config

This script is designed to identify switch ports with a certain configuration and change them as desired for switches running IOS.

For example, the current version of this script imagines a scenario where the VLANs for switch ports needs to be changed from their current VLAN to a new one.

Ordinarily, this would be a tedious, time-consuming process that’s prone to unpredictable human error. This script aims to remove that by allowing engineers at any level of experience with automation by removing the logical, programmatic layer and just letting them update a simple data file.

![script](https://raw.githubusercontent.com/pduffman004/cisco_switchport_config/master/static/script.gif)
 
This script can loop over multiple switches, switch stacks, and even multiple IDFs.

### Before
![Before](https://raw.githubusercontent.com/pduffman004/cisco_switchport_config/master/static/before.png)

### After
![After](https://raw.githubusercontent.com/pduffman004/cisco_switchport_config/master/static/after.png)

This script can also be modified to audit other switch port configurations, like ensuring access ports have “spanning-tree bpduguard enable” or even to check whether ACLs are applied for SSH access to the devices.

  
A more technical explanation can be found in the documentation.
> Written with [StackEdit](https://stackedit.io/).
