
# Documentation

This documentation assumes you're reading this after the readme and will provide a brief overview of the more technical details of the tools used in this script. This article will stick with a high level discussion; more in-depth details of the code can be found in the python file comments.
## Switch Data Organization
As this is designed to be a lightweight, ad hoc sort-of tool, the information on the switches to be configured is stored in the switch_info.json file in the source folder and is the only file that needs to be edited by the tech or engineer running the script. The JSON file is broken up into a list of dictionaries, with each dictionary representing an IDF or building floor in a campus network. In this case, the network is being imagined with different floors and an IDF on each one. The JSON file contains the current VLAN numbers configured on the switches, the new ones that they should be changed to, and finally a nested list of dictionaries with the hostname and management IPs of each switch, which will be used for SSH access.

![enter image description here](https://previews.dropbox.com/p/thumb/AAb7kJ1lWiW5KUt8y65mwfCDMU9lPT7uX6haup5PPd8ncBqA9KuKsrDUcuZ1V5WWrHhi-3k1oOFisQIKEgW4AcsbqowKP-mBbWWoWJ6V0734X4Irbzy9cGKb9df5wKoMWzD2FAsw9KstcKTRQnsZcJbxX59luu-FjZLv3nHupdYC-MTxIv6CtYB6Ner5anW8pnn9UPR7kHGb9xQYpjFqW6egz4eqJ30Kwri97OOpSCcyXfximEV5mH4nGwKHVpMfN1KZ-W8Z0M372ArEGfhqHyAq6OXYFNeGkqSXGARDMBbJ76HGpvLuZzz-BaqYkLf7m226JT9Ml3Oe7OlF-hBXx1fCDNfWbn4gkRjcmFTwAYg26ZnZ7YYYfgrEI-o6bbyZQeXxoDl2G1-KlvaErSJcdlf0IXc4uwXGfWZ6a4fW6I5-nA/p.png?fv_content=true&size_mode=5)
## Connection and Config Parsing
Next, the script uses Napalm's python module to handle connections to each switch as well as facilitating issuing read and write (show and config) commands . The information from the JSON file is passed through to the connection so the script can loop through each switch in each IDF (or "floor") and then proceed to the next IDF and continue with each switch there.

During this process, Napalm is used to gather the current running configuration, which is then parsed using the CiscoConfParse python module and also saved to the tech's local machine in case it's needed for reference. The script identifies every interface configured with the VLANs stated in the JSON file to find configurations associated with the interface, like "switchport access vlan 10". A list is compiled of all the interfaces that need to be changed.
## Compiling The New Configuration
Next, the list of interfaces that need to be re-configured is passed through a Jinja template, which can be found in conf_template.j2. The template sets commands to add the new VLANs to the switch, iterates over the list of ports to be edited, and builds configuration commands depending on what VLAN the interface needs to be changed to.

![enter image description here](https://previews.dropbox.com/p/thumb/AAZN8zp1vt-9xZlBpLTkIwqe2mzKhVTj9rRJ2T8YI57dviBLYjQaDiW54RGkiViksw21PYaVmH29F1fcBbdbqzHDKZ5ONo7L7QzrZsmpMZxpj_GdHuecBV5dOXc6GEgMwsFOnZCPKvT10-Jpycr6QEnLHNrvnYZyLrlDcUCnc0yue4_6QoHjrwYV2XKZbJwAPPLC22RXDK58VU0WECeUyUsNevq6s-q8pzfapH9kDgRTuCR2s-KObHIs9nl6lubY3oXXxOlctMBQz2zRTo5YdwU-bZEWnmhw9h-1lpxjoF-z3AlIFlrclgfv5b9BlXBIPKprnnqXVEqC5CDi9K7_QtPBWG5eE0NSOk84tkaqOfhMU1t92UrcTMVW_eghKjVlBo0a8Ed09g6UbfLZsfj5LRQpM1Ng7KvLeX2LDGr8ZeSgCA/p.png?fv_content=true&size_mode=5)

The configuration changes compiled using the Jinja template are finally passed through to the Switch using Napalm and the net changes are printed to the console so that the tech can approve or discard the changes before they're committed.

> Written with [StackEdit](https://stackedit.io/).
