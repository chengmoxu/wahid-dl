import os
from packages.core import ui
from packages.core import version_info
from packages.core import system_os
system_os = system_os.get_system_os()
def wahiddl_devmode_windows():
    print(ui.ASCII_art())
    print(ui.get_title_wahiddl_devmode())
    print ("------------------------------------------------------------")
    mode = "start"
    while mode == "start":
        print ("wahid-dl Dev Mode，請直接輸入wahid-dl命令或是yt-dlp命令")
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
            if userinput.startswith("yt-dlp") == True:
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
            if userinput.startswith("wahid-dl -V") == True:
                print (version_info.get_version_detail())
                print ("------------------------------------------------------------")
            else:
                print ("請重新輸入正確命令！")
                mode = "start"    
        else:
            print ("請重新輸入正確命令！")
            mode = "start"
    while mode == "end":
        print ("------------------------------------------------------------")
        print("即將結束程式")
        print ("------------------------------------------------------------")
        break