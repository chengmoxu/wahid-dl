# wahid-dl Dev Mode
'''
      ###       ###        ###         ###     ###         #######      ########             #########       ###
     ###       ###      ###   ##      ###     ###         ###          ###    ###           ###    ###      ###
    ###       ###     ###    ##      ###     ###         ###          ###    ###           ###    ###      ###
   >>>  >>>  >>>    >>>>>>>>>>>     >>>>>>>>>>>         >>>          >>>    >>>   >>>>>   >>>    >>>      >>>
  ### ##  # ###    ###      ##     ###     ###         ###          ###    ###           ###    ###      ###
 #####    ###     ###      ##     ###     ###         ###          ###    ###           ###    ###      ###
####      ##     ###      ##     ###     ###     #######          #########            #########       ###
'''

import os
from packages.checking import checking_system_os
from packages.core import wahiddl_devmode
system_os = checking_system_os.get_system_os()
print (system_os)
if system_os  == "Windows":
    wahiddl_devmode.wahiddl_devmode_windows()
elif system_os  == "Linux":
    print ('暫時不支援')
elif system_os == "macOS":
    print ('暫時不支援')
else:
    print ('不支援的平台')
os.system ('pause')