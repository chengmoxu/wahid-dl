import os
from packages.core import ui
def wahiddl():
    print(ui.ASCII_art())
    print(ui.ui_title_wahiddl())
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
                mode = ""
        elif userinput_judge == False:
            if userinput.startswith("http") == True:
                print ("------------------------------------------------------------")
                print ("執行開始")
                print ("------------------------------------------------------------")
                os.chdir ('C:\\wahid-dl')
                downloadcommand = str (('yt-dlp -c -S"quality,res,fps,hdr:12,channels,size,br,asr" --throttled-rate 100K --merge-output-format mp4 --ffmpeg-location "C:\\FFmpeg" ') + userinput)
                os.system (downloadcommand)
                ui.ui_complete()
            elif userinput.startswith("http") == False:
                print ("請重新輸入正確網址！")
            else:
                print ("請重新輸入正確網址！") 
        else:
            print ("請重新輸入正確命令！")
            mode = ""
    while mode == "0":
        ui.ui_exit()
        break