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
from packages.core import title

# Download Function within OS judge
if sys.platform == "win32":
    print (title.get_title_wahiddl())
    print ("------------------------------------------------------------")
    mode = ""
    while mode == "":
        print ("請輸入欲下載影片之網址")
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
                downloadcommand = str (('yt-dlp -c -S"quality,res,fps,hdr:12,channels,size,br,asr" --throttled-rate 100K --merge-output-format mp4 --ffmpeg-location "C:\\FFmpeg" ') + userinput)
                os.system (downloadcommand)
                print ("------------------------------------------------------------")
                print ("執行結束，請至資料夾內確認您的下載")
                print ("------------------------------------------------------------")
            elif userinput.startswith("http") == False:
                print ("請重新輸入正確網址！")
            else:
                print ("請重新輸入正確網址！")
    while mode == "0":
        print("即將結束程式，稍後再次按下Enter鍵即可退出此程式")
        break
elif sys.platform == "linux":
    print (title.get_title_wahiddl())
    print ("------------------------------------------------------------")
    mode = ""
    while mode == "":
        print ("Please enter the URL of the video you want to download")
        print ("Or enter '0' to end this program\n")
        userinput = input ("Please enter:")
        userinput_judge = str.isdigit(userinput)
        if userinput_judge == True: 
            if  userinput == "0":
                mode = "0"
            else:
               print ("Please re-enter the correct options!")
        elif userinput_judge == False:
            if userinput.startswith("http") == True:
                print ("------------------------------------------------------------")
                print ("Execution starts")
                print ("------------------------------------------------------------")
                downloadcommand = str (('yt-dlp -c -S"quality,res,fps,hdr:12,channels,size,br,asr" --throttled-rate 100K --merge-output-format mp4 ') + userinput)
                os.system (downloadcommand)
                print ("------------------------------------------------------------")
                print ("The execution is completed, please go to the folder to confirm your download")
                print ("------------------------------------------------------------")
            elif userinput.startswith("http") == False:
                print ("Please re-enter the correct URL!")
            else:
                print ("Please re-enter the correct URL!")
    while mode == "0":
        print("This program will come to a close, press the Enter key again later to exit this program")
        break
#elif sys.platform == "darwin":
#    print ("wahid-dl Python-Based")
input()