# wahid-dl-python-based for Quality Selection
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

# Quality Selection within OS judge
if sys.platform == "win32":
    print ("wahid-dl-python-based for Quality Selection")
    print ("------------------------------------------------------------")
    mode = ""
    while mode != "0":
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
                testcommand = str (('yt-dlp -F ') + userinput)
                os.system (testcommand)
                print ('請記下您想要下載的影片畫質ID，並於下方輸入')
                print ('若有疑問，請參閱 https://github.com/chengmoxu/wahid-dl 說明文件')
                video_quality_id = str(input('請輸入影片畫質ID:'))
                command = str (('yt-dlp -c -f "') + video_quality_id + ('+bestaudio[ext=m4a]" --throttled-rate 100K --merge-output-format mp4 --ffmpeg-location "C:\\FFmpeg" ') + userinput)
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
    print ("wahid-dl-python-based for Quality Selection")
    print ("------------------------------------------------------------")
    mode = ""
    while mode != "0":
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
                subprocess.check_call ([sys.executable, '-m', 'pip', 'install', '-U', 'yt-dlp[default]'])
                testcommand = str (('yt-dlp -F ') + userinput)
                os.system (testcommand)
                print ('請記下您想要下載的影片畫質ID，並於下方輸入')
                print ('若有疑問，請參閱 https://github.com/chengmoxu/wahid-dl 說明文件')
                video_quality_id = str(input('請輸入影片畫質ID:'))
                command = str (('yt-dlp -c -f "') + video_quality_id + ('+bestaudio[ext=m4a]" --throttled-rate 100K --merge-output-format mp4 --ffmpeg-location "C:\\FFmpeg" ') + userinput)
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