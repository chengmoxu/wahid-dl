# wahid-dl Python-Based Dev Mode
# Version: 4.1
# Build: wahid-dl.v4.1.20240703.Python.1
'''
      ###       ###        ###         ###     ###         #######      ########             #########       ###
     ###       ###      ###   ##      ###     ###         ###          ###    ###           ###    ###      ###
    ###       ###     ###    ##      ###     ###         ###          ###    ###           ###    ###      ###
   >>>  >>>  >>>    >>>>>>>>>>>     >>>>>>>>>>>         >>>          >>>    >>>   >>>>>   >>>    >>>      >>>
  ### ##  # ###    ###      ##     ###     ###         ###          ###    ###           ###    ###      ###
 #####    ###     ###      ##     ###     ###         ###          ###    ###           ###    ###      ###
####      ##     ###      ##     ###     ###     #######          #########            #########       ###
[Stable] v4.1.20240703.Python.1

'''

# Library import
import os
import sys
import subprocess

# Download Function within OS judge
if sys.platform == "win32":
    print ("wahid-dl Python-Based Dev Mode [Windows]")
    print ("Version: 4.1")
    print ("Build: wahid-dl.v4.1.20240703.Python.1")
    print ("------------------------------------------------------------")
    mode = ""
    while mode != "0":
        print ("yt-dlp命令模式，請直接輸入yt-dlp命令")
        print ("或者，想要結束程式請輸入0\n")
        userinput = input ("請輸入：")
        userinput_judge = str.isdigit(userinput)
        if userinput_judge == True: 
            if  userinput == "0":
                mode = "0"
            else:
               print ("請重新輸入正確選項！")
        elif userinput_judge == False:
            print ("------------------------------------------------------------")
            print ("執行開始")
            print ("------------------------------------------------------------")
            os.chdir ('C:\\wahid-dl')
            subprocess.check_call ([sys.executable, '-m', 'pip', 'install', '-U', 'yt-dlp[default]'])
            command = str (('yt-dlp ') + userinput)
            os.system (command)
            print ("------------------------------------------------------------")
            print ("執行結束，請至資料夾內確認您的下載")
            print ("------------------------------------------------------------")
        else:
            print ("請重新輸入正確命令！")
    while mode == "0":
        print("即將結束程式")
        break
elif sys.platform == "linux":
    print ("wahid-dl Python-Based Dev Mode [Linux]")
    print ("Version: 4.1")
    print ("Build: wahid-dl.v4.1.20240628.Python.1")
    print ("------------------------------------------------------------")
    mode = ""
    while mode != "0":
        print ("yt-dlp命令模式，請直接輸入yt-dlp命令")
        print ("或者，想要結束程式請輸入0\n")
        userinput = input ("請輸入：")
        userinput_judge = str.isdigit(userinput)
        if userinput_judge == True: 
            if  userinput == "0":
                mode = "0"
            else:
               print ("請重新輸入正確選項！")
        elif userinput_judge == False:
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
    while mode == "0":
        print("即將結束程式")
        break
#elif sys.platform == "darwin":
#    print ("macOS Mode")
os.system ('pause')