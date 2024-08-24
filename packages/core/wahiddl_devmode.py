import os
from packages.checking import checking_system_os
from packages.core import version_info
system_os = checking_system_os.get_system_os()
def wahiddl_devmode_windows():
    print("wahid-dl Dev Mode [" + system_os + "]")
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