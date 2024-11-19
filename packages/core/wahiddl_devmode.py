import os
from packages.core import ui
from packages.core import version_info
from packages.core import system_os
system_os = system_os.get_system_os()
def devmode():
    print(ui.ASCII_art())
    print(ui.get_title_wahiddl_devmode())
    print ("------------------------------------------------------------")
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
                if system_os == "Windows":
                    os.chdir ('C:\\wahid-dl')
                elif system_os == "Linux":
                    os.chdir ('$HOME/wahid-dl')
                else:
                    continue
                command = str (('yt-dlp ') + userinput)
                os.system (command)
                ui.ui_complete()
                mode = ""
            if userinput.startswith("wahid-dl -V") == True:
                print (version_info.version_detail())
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