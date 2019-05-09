

# Cisco Switchport Config

This script is designed to identify switch ports with a certain configuration and change them as desired for switches running IOS.

For example, the current version of this script imagines a scenario where the VLANs for switch ports needs to be changed from their current VLAN to a new one.

Ordinarily, this would be a tedious, time-consuming process that’s prone to unpredictable human error. This script aims to remove that by allowing engineers at any level of experience with automation by removing the logical, programmatic layer and just letting them update a simple data file.

 <iframe src="https://giphy.com/embed/1yjq26jbvaF47tmjWm" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p></p>  
 
This script can loop over multiple switches, switch stacks, and even multiple IDFs.

### Before
![enter image description here](https://previews.dropbox.com/p/thumb/AAYlJwujJnFY4who1iKqun7snjVMIhMxD-lqFTL1QDFAmzDlbGgGcIaNWJljFd47iuA3pU52hyPAUUHkD2vWxKY2i7vtW0igMzVwhmcA7sUsL_VbMg41Y8Wz7hmZjbBHHRNmRn4_mxCkqqHs3w5AIg68OjiCa3kTt0V8ARNr4duzlOqJdUr9iENkT2_LFKcQpfqNqtshfVI30gSeiLa-7DbZLGMUu2f5qeAXrxwNDHMCHVbeYH_9nSE80P0vQaXxKfxNMrwkARBRzQJwarmI9MsN3zHOAjjacCF5ox9sbcHzgehZiOCak9vbqQ5IYK_hVngj3CKbS7hoXwVvkfzfKfc5Ek8pPl5-oveLf-zEWc2490UCdo9brQnuDbVcVsnFVc4xyHquIvrUZp3NvVUSm5t5eHaUy6bm3a7L5VsXIa2AnQ/p.png?fv_content=true&size_mode=5)

### After
![image](https://www.dropbox.com/s/j0eenjakn2n8uxe/json_file.png?dl=0)

This script can also be modified to audit other switch port configurations, like ensuring access ports have “spanning-tree bpduguard enable” or even to check whether ACLs are applied for SSH access to the devices.

  
A more technical explanation can be found in the documentation.
> Written with [StackEdit](https://stackedit.io/).
