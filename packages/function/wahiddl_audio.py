import os
from packages.core import ui
def main():
    print(ui.ASCII_art())
    print(ui.ui_title_wahiddl_audio())
    print ("------------------------------------------------------------")
    mode = ""
    while mode == "":
        print ("請輸入欲下載音訊之網址")
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
                downloadcommand = str (('yt-dlp -c --throttled-rate 100K --extract-audio -f "bestaudio[ext=m4a]" ') + userinput)
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