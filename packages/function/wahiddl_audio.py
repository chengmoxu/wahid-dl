import os
import subprocess
from packages.core import ui
from packages.core import path #unified path function
from packages.core import command
def main():
    print(ui.ASCII_art())
    print(ui.detail_wahiddl_audio())
    mode = ""
    while mode == "":
        print(ui.divider())
        print("請輸入欲下載音訊之網址")
        print("或者，請輸入0結束程式\n")
        userinput = input("請輸入：")
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
                downloadcommand = str(command.wahiddl_audio() + userinput)
                subprocess.run(downloadcommand)
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