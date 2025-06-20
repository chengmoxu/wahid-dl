import os
from packages.core import ui
def main():
    print(ui.ASCII_art())
    print(ui.ui_title_wahiddl_subtitle())
    print ("------------------------------------------------------------")
    mode = ""
    while mode == "":
        print ("請輸入欲下載影片字幕之網址")
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
                ui.ui_start()
                os.chdir ('C:\\wahid-dl')
                testcommand = str (('yt-dlp --list-subs ') + userinput)
                os.system (testcommand)
                print ('請記下您想要下載的影片字幕Language，並於下方輸入')
                print ('若有疑問，請參閱 https://github.com/chengmoxu/wahid-dl 說明文件')
                video_sub_id = str(input('請輸入影片字幕Language:'))
                command = str (('yt-dlp -c --sub-lang ') + video_sub_id + (' --write-subs --skip-download ') + userinput)
                os.system (command)
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