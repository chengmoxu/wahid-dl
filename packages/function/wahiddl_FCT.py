import os
from packages.core import ui
from packages.core import path #unified path function
def main():
    print(ui.ASCII_art())
    print(ui.ui_title_wahiddl_FCT())
    print ('--------------------------------------------------')
    mode = ""
    while mode == "":
        print ("請輸入欲測試影片或音檔之網址")
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
                os.chdir (path.wahiddl_folder())
                testcommand = str (('yt-dlp -F ') + userinput)
                os.system (testcommand)
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