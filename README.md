

# Cisco Switchport Config

This script is designed to identify switch ports with a certain configuration and change them as desired for switches running IOS.

For example, the current version of this script imagines a scenario where the VLANs for switch ports needs to be changed from their current VLAN to a new one.

Ordinarily, this would be a tedious, time-consuming process that’s prone to unpredictable human error. This script aims to remove that by allowing engineers at any level of experience with automation by removing the logical, programmatic layer and just letting them update a simple data file.

 <iframe src="https://giphy.com/embed/1yjq26jbvaF47tmjWm" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p></p>  
 
This script can loop over multiple switches, switch stacks, and even multiple IDFs.

### Before
![enter image description here](https://previews.dropbox.com/p/thumb/AAYlJwujJnFY4who1iKqun7snjVMIhMxD-lqFTL1QDFAmzDlbGgGcIaNWJljFd47iuA3pU52hyPAUUHkD2vWxKY2i7vtW0igMzVwhmcA7sUsL_VbMg41Y8Wz7hmZjbBHHRNmRn4_mxCkqqHs3w5AIg68OjiCa3kTt0V8ARNr4duzlOqJdUr9iENkT2_LFKcQpfqNqtshfVI30gSeiLa-7DbZLGMUu2f5qeAXrxwNDHMCHVbeYH_9nSE80P0vQaXxKfxNMrwkARBRzQJwarmI9MsN3zHOAjjacCF5ox9sbcHzgehZiOCak9vbqQ5IYK_hVngj3CKbS7hoXwVvkfzfKfc5Ek8pPl5-oveLf-zEWc2490UCdo9brQnuDbVcVsnFVc4xyHquIvrUZp3NvVUSm5t5eHaUy6bm3a7L5VsXIa2AnQ/p.png?fv_content=true&size_mode=5)

### After
![enter image description here](https://previews.dropbox.com/p/thumb/AAajLIUCTxL1zGQ7RwAAXiiCC58T2RZvk_1IU9qOakLB8x0oSXPQJ2CFM72JwlItjzIzMWscuy6Cr9Oi-A1_mZaqDHUO2CMhpRX30HG72qUiEpu7LjQeSVStqN7Yf4hq5fLbRQfUNdH1BdfgX_8b73Ff9Aj5jNKEF-dZ90eelOfFi8U66FncI-EjsOpG-UmLANOaXCx1zTZJEfVGGMeiMJ1iHR-tf4q-i1dWCa45TQcYaO2QNaUk3Kbwe3uhYJ3CpWul5xqHmYF-8slY98eu737TcjQkgUbBledHHoQTUQtmHHvyFmrsUY5oXf1SdzSPAkAeXnBu7TY9fhfmvkbZXsKTNo5OiKgH5Xy5jEH_w_pXqUY37mRx2G9QB8QTOCIJDxQPgu3rm_QBSTIa-MrzZ6S9OiqObY2OQAs1zpM_Uuhdyg/p.png?fv_content=true&size_mode=5)

This script can also be modified to audit other switch port configurations, like ensuring access ports have “spanning-tree bpduguard enable” or even to check whether ACLs are applied for SSH access to the devices.

  
A more technical explanation can be found in the documentation.
> Written with [StackEdit](https://stackedit.io/).
