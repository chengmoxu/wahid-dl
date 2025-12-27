import os
import sys
from packages.core import ui
from packages.core import version_info
from packages.core import path #unified path function
def devmode():
    print(ui.ASCII_art())
    print(ui.ui_title_wahiddl_devmode())
    print ('--------------------------------------------------')
    mode = ""
    while mode == "":
        print ("wahid-dl Dev Mode，請直接輸入wahid-dl命令或是yt-dlp命令")
        print ("或者，請輸入0結束程式\n")
        userinput = input ("請輸入：")
        userinput_judge = str.isdigit(userinput)
        if userinput_judge == True:
            if  userinput == "0":
                mode = "0"
            else:
                print ("請重新輸入正確選項！")
                mode = ""
        elif userinput_judge == False:
            if userinput.startswith("yt-dlp") == True:
                ui.ui_start()
                if sys.platform == "win32":
                    os.chdir (path.wahiddl_folder())
                elif sys.platform == "linux":
                    os.chdir ('$HOME/wahid-dl')
                else:
                    continue
                command = str (('yt-dlp ') + userinput)
                os.system (command)
                ui.ui_complete()
                mode = ""
            if userinput.startswith("wahid-dl -V") == True:
                print ("Channel: " + version_info.vi_detail()[0] + "\n" + "Version Number: " + version_info.vi_detail()[1] + "\n" + "Build Number: " + version_info.vi_detail()[2] + "\n" + "Language: " + version_info.vi_detail()[3])
                ui.ui_complete()
                mode = ""
            else:
                print ("請重新輸入正確命令！")
                mode = ""    
        else:
            print ("請重新輸入正確命令！")
            mode = ""
    while mode == "0":
        ui.ui_exit()
        break