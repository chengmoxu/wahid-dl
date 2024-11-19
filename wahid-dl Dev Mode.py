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

from packages.core import system_os
from packages.core import wahiddl_devmode
system_os = system_os.get_system_os()
if system_os  == "Windows":
    wahiddl_devmode.devmode()
elif system_os  == "Linux":
    wahiddl_devmode.devmode()
elif system_os == "macOS":
    print ("暫時不支援")
else:
    print ("不支援的平台")
input()