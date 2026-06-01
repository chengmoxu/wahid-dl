import os
import sys
import subprocess
from packages.core import ui
from packages.core import info
from packages.core import path #unified path function
def devmode():
    print(ui.ASCII_art())
    print(ui.detail_wahiddl_devmode())
    mode = ""
    while mode == "":
        print(ui.divider())
        print("wahid-dl Dev Mode，請直接輸入wahid-dl命令或是yt-dlp命令")
        print("或者，請輸入0結束程式\n")
        userinput = input ("請輸入：")
        userinput_judge = str.isdigit(userinput)
        if userinput_judge == True:
            if  userinput == "0":
                mode = "0"
            else:
                print("請重新輸入正確選項！")
                mode = ""
        elif not userinput_judge:
            if userinput.startswith("yt-dlp") == True:
                ui.start()
                if sys.platform == "win32":
                    os.chdir(path.wahiddl_folder())
                elif sys.platform == "linux":
                    os.chdir('$HOME/wahid-dl')
                else:
                    continue
                command = ['yt-dlp', userinput]
                subprocess.run(command)
                print(ui.complete())
                mode = ""
            if userinput.startswith("wahid-dl -V") == True:
                print("Channel: " + info.version_detail()[0] + "\n" + "Version Number: " + info.version_detail()[1] + "\n" + "Build Number: " + info.version_detail()[2] + "\n" + "Programming Language: " + info.version_detail()[3])
                print(ui.complete())
                mode = ""
            else:
                print("請重新輸入正確命令！")
                mode = ""    
        else:
            print("請重新輸入正確命令！")
            mode = ""
    while mode == "0":
        ui.exit()
        break