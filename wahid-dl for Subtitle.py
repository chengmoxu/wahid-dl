import os
import sys
from packages.core import ui

if sys.platform == "win32":
    print (ui.ASCII_art())
    print (ui.get_title_wahiddl_QS())
    print ("------------------------------------------------------------")
    mode = ""
    while mode != "0":
        print ("請輸入欲下載影片字幕之網址")
        print ("或者，請輸入0結束程式\n")
        userinput = input ("請輸入：")
        userinput_judge = str.isdigit(userinput)
        if userinput_judge == True: 
            if  userinput == "0":
                mode = "0"
            else:
               print ("請重新輸入正確選項！")
        elif userinput_judge == False:
            if userinput.startswith("http") == True:
                print ("------------------------------------------------------------")
                print ("執行開始")
                print ("------------------------------------------------------------")
                os.chdir ('C:\\wahid-dl')
                testcommand = str (('yt-dlp --list-subs ') + userinput)
                os.system (testcommand)
                print ('請記下您想要下載的影片字幕Language，並於下方輸入')
                print ('若有疑問，請參閱 https://github.com/chengmoxu/wahid-dl 說明文件')
                video_sub_id = str(input('請輸入影片字幕Language:'))
                command = str (('yt-dlp -c --sub-lang ') + video_sub_id + (' --write-subs --skip-download ') + userinput)
                os.system (command)
                print ("------------------------------------------------------------")
                print ("執行結束")
                print ("------------------------------------------------------------")
            elif userinput.startswith("http") == False:
                print ("請重新輸入正確網址！")
            else:
                print ("請重新輸入正確網址！")
    while mode == "0":
        print("即將結束程式")
        break
elif sys.platform == "linux":
    print (ui.ASCII_art())
    print (ui.get_title_wahiddl_QS())
    print ("------------------------------------------------------------")
    mode = ""
    while mode != "0":
        print ("請輸入欲下載影片字幕之網址")
        print ("或者，請輸入0結束程式\n")
        userinput = input ("請輸入：")
        userinput_judge = str.isdigit(userinput)
        if userinput_judge == True: 
            if  userinput == "0":
                mode = "0"
            else:
               print ("請重新輸入正確選項！")
        elif userinput_judge == False:
            if userinput.startswith("http") == True:
                print ("------------------------------------------------------------")
                print ("執行開始")
                print ("------------------------------------------------------------")
                
                testcommand = str (('yt-dlp --list-subs ') + userinput)
                os.system (testcommand)
                print ('請記下您想要下載的影片字幕Language，並於下方輸入')
                print ('若有疑問，請參閱 https://github.com/chengmoxu/wahid-dl 說明文件')
                video_sub_id = str(input('請輸入影片字幕Language:'))
                command = str (('yt-dlp -c --sub-lang ') + video_sub_id + (' --write-subs --skip-download ') + userinput)
                os.system (command)
                print ("------------------------------------------------------------")
                print ("執行結束")
                print ("------------------------------------------------------------")
            elif userinput.startswith("http") == False:
                print ("請重新輸入正確網址！")
            else:
                print ("請重新輸入正確網址！")
    while mode == "0":
        print("即將結束程式")
        break
#elif sys.platform == "darwin":
#    print ("wahid-dl Python-Based")
os.system ('pause')