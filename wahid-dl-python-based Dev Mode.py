# wahid-dl Python-Based Dev Mode
# [Dev] v4.6.20240816.Python.1
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
import subprocess

# Dev Mode within OS judge
if sys.platform == "win32":
    print ("wahid-dl Python-Based Dev Mode [Windows]")
    print ("[Stable] v4.5.20240816.Python.1")
    print ("------------------------------------------------------------")
    mode = "Start"
    mode_con = ""
    while mode == "Start":
        print ("yt-dlp命令模式，請直接輸入yt-dlp命令")
        print ("或者，請輸入0結束程式\n")
        userinput = input ("請輸入：")
        userinput_judge = str.isdigit(userinput)
        if userinput_judge == True: 
            if  userinput == "0":
                mode = "0"
                mode_con = "0"
            else:
               print ("請重新輸入正確選項！")
        elif userinput_judge == False:
            if userinput == "wahiddl -V" or "wahiddl --version":
                mode = "versioninfo"
            else:
                print ("------------------------------------------------------------")
                print ("執行開始")
                print ("------------------------------------------------------------")
                os.chdir ('C:\\wahid-dl')
                command = str (('yt-dlp ') + userinput)
                os.system (command)
                print ("------------------------------------------------------------")
                print ("執行結束，請至資料夾內確認您的下載")
                print ("------------------------------------------------------------")
        else:
            print ("請重新輸入正確命令！")
    while mode == "versioninfo":
        versioninfo_detail = str ("[DEV] v4.4.20240812.Python.2")
        print (versioninfo_detail)
        mode_con = "0"
        if mode_con == "0":
            mode = "0"
        elif mode_con == "1":
            mode = "0"
    while mode == "0":
        print("即將結束程式")
        break
elif sys.platform == "linux":
    print ("wahid-dl Python-Based Dev Mode [Linux]")
    print ("[Stable] v4.5.20240816.Python.1")
    print ("------------------------------------------------------------")
    mode = "Start"
    mode_con = ""
    while mode == "Start":
        print ("yt-dlp命令模式，請直接輸入yt-dlp命令")
        print ("或者，請輸入0結束程式\n")
        userinput = input ("請輸入：")
        userinput_judge = str.isdigit(userinput)
        if userinput_judge == True: 
            if  userinput == "0":
                mode = "0"
                mode_con = "0"
            else:
               print ("請重新輸入正確選項！")
        elif userinput_judge == False:
            if userinput == "wahiddl -V" or "wahiddl --version":
                mode = "versioninfo"
            else:
                print ("------------------------------------------------------------")
                print ("執行開始")
                print ("------------------------------------------------------------")
                subprocess.check_call ([sys.executable, '-m', 'pip', 'install', '-U', 'yt-dlp[default]'])
                command = str (('yt-dlp ') + userinput)
                os.system (command)
                print ("------------------------------------------------------------")
                print ("執行結束，請至資料夾內確認您的下載")
                print ("------------------------------------------------------------")
        else:
            print ("請重新輸入正確命令！")
    while mode == "versioninfo":
        versioninfo_detail = str ("[DEV] v4.4.20240812.Python.2")
        print (versioninfo_detail)
        mode_con = "0"
        if mode_con == "0":
            mode = "0"
        elif mode_con == "1":
            mode = "0"
    while mode == "0":
        print("即將結束程式")
        break
#elif sys.platform == "darwin":
#    print ("macOS Mode")
os.system ('pause')