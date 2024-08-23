# wahid-dl Python-Based Dev Mode
# [Dev] v4.7-20240823.1
'''
      ###       ###        ###         ###     ###         #######      ########             #########       ###
     ###       ###      ###   ##      ###     ###         ###          ###    ###           ###    ###      ###
    ###       ###     ###    ##      ###     ###         ###          ###    ###           ###    ###      ###
   >>>  >>>  >>>    >>>>>>>>>>>     >>>>>>>>>>>         >>>          >>>    >>>   >>>>>   >>>    >>>      >>>
  ### ##  # ###    ###      ##     ###     ###         ###          ###    ###           ###    ###      ###
 #####    ###     ###      ##     ###     ###         ###          ###    ###           ###    ###      ###
####      ##     ###      ##     ###     ###     #######          #########            #########       ###
'''

# Library import
import os
import sys
from packages.core import version_info

def wahiddl_devmode_core():
    system_os = ""
    if sys.platform  == "win32":
        system_os = "Windows"
    elif sys.platform  == "linux":
        system_os = "Linux"
    elif sys.platform == "darwin":
        system_os = "macOS"
    print("wahid-dl Python-Based Dev Mode [" + system_os + "]")
    display_version_outline = version_info.get_version_outline()
    print (display_version_outline)
    print ("------------------------------------------------------------")
    mode = "start"
    while mode == "start":
        print ("wahid-dl Python-Based Dev Mode，請直接輸入wahid-dl命令或是yt-dlp命令")
        print ("或者，請輸入0結束程式\n")
        userinput = input ("請輸入：")
        userinput_judge = str.isdigit(userinput)
        if userinput_judge == True:
            if  userinput == "0":
                mode = "end"
            else:
                print ("請重新輸入正確選項！")
                mode = "start"
        elif userinput_judge == False:
            if userinput == "wahid-dl -V" or "wahid-dl --version":
                display_version_outline = version_info.get_version_outline()
                print (display_version_outline)
                print ("------------------------------------------------------------")
            else:
                print ("------------------------------------------------------------")
                print ("執行開始")
                print ("------------------------------------------------------------")
                if system_os == "Windows":
                    os.chdir ('C:\\wahid-dl')
                else:
                    continue
                command = str (('yt-dlp ') + userinput)
                os.system (command)
                print ("------------------------------------------------------------")
                print ("執行結束")
                print ("------------------------------------------------------------")
        else:
            print ("請重新輸入正確命令！")
            mode = "start"
    while mode == "end":
        print ("------------------------------------------------------------")
        print("即將結束程式")
        print ("------------------------------------------------------------")
        break

wahiddl_devmode_core()
os.system ('pause')