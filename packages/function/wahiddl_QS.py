import os
from packages.core import ui
from packages.core import path #unified path function
from packages.core import command
def main():
    print(ui.ASCII_art())
    print(ui.detail_wahiddl_QS())
    mode = ""
    while mode == "":
        print(ui.divider())
        print("請輸入欲下載影片之網址")
        print("或者，請輸入0結束程式\n")
        userinput = input ("請輸入：")
        userinput_judge = str.isdigit(userinput)
        if userinput_judge == True:
            if  userinput == "0":
                mode = "0"
            else:
                print("請重新輸入正確選項！")
                mode = ""
        elif userinput_judge == False:
            if userinput.startswith("http") == True:
                ui.start()
                os.chdir(path.wahiddl_folder())
                testcommand = str(command.wahiddl_QS()[0] + userinput)
                os.system(testcommand)
                print('請記下您想要下載的影片畫質ID，並於下方輸入')
                print('若有疑問，請參閱 https://github.com/chengmoxu/wahid-dl 或 https://github.com/yt-dlp/yt-dlp 說明文件')
                video_quality_id = str(input('請輸入影片畫質ID:'))
                downloadcommand = str(command.wahiddl_QS()[1] + video_quality_id + command.wahiddl_QS()[2] + userinput)
                os.system(downloadcommand)
                ui.complete()
            elif userinput.startswith("http") == False:
                print("請重新輸入正確網址！")
            else:
                print("請重新輸入正確網址！") 
        else:
            print("請重新輸入正確命令！")
            mode = ""
    while mode == "0":
        print(ui.exit())
        break