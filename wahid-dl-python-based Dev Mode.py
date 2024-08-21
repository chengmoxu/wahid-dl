# wahid-dl Python-Based Dev Mode
# [Dev] v4.7.20240821.Python.2
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

# Dev Mode within OS judge
if sys.platform == "win32":
    print ("wahid-dl Python-Based Dev Mode [Windows]")
    print ("[Dev] v4.7.20240821.Python.2")
    print ("------------------------------------------------------------")
    mode = "Start"
    mode_con = ""
    while mode == "Start":
        print ("wahid-dl Python-Based Dev Mode，請直接輸入wahid-dl命令或是yt-dlp命令")
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
            if userinput == "wahid-dl -V" or "wahid-dl --version":
                mode = "versioninfo"
            else:
                print ("------------------------------------------------------------")
                print ("執行開始")
                print ("------------------------------------------------------------")
                os.chdir ('C:\\wahid-dl')
                command = str (('yt-dlp ') + userinput)
                os.system (command)
                print ("------------------------------------------------------------")
                print ("執行結束")
                print ("------------------------------------------------------------")
        else:
            print ("請重新輸入正確命令！")
    while mode == "versioninfo":
        versioninfo_detail = str ("[Dev] v4.7.20240821.Python.2")
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
    print ("[Dev] v4.7.20240821.Python.2")
    print ("------------------------------------------------------------")
    mode = "Start"
    mode_con = ""
    while mode == "Start":
        print ("wahid-dl Python-Based Dev Mode，請直接輸入wahid-dl命令或是yt-dlp命令")
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
            if userinput == "wahid-dl -V" or "wahid-dl --version":
                mode = "versioninfo"
            else:
                print ("------------------------------------------------------------")
                print ("執行開始")
                print ("------------------------------------------------------------")
                command = str (('yt-dlp ') + userinput)
                os.system (command)
                print ("------------------------------------------------------------")
                print ("執行結束")
                print ("------------------------------------------------------------")
        else:
            print ("請重新輸入正確命令！")
    while mode == "versioninfo":
        versioninfo_detail = str ("[Dev] v4.7.20240821.Python.2")
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