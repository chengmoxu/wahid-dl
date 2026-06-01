import os
import subprocess
from packages.core import ui
from packages.core import path #unified path function
from packages.core import command
def main():
    print(ui.ASCII_art())
    print(ui.detail_wahiddl_FCT())
    mode = ""
    while mode == "":
        print(ui.divider())
        print("請輸入欲測試影片或音檔之網址")
        print("或者，請輸入0結束程式\n")
        userinput = input("請輸入：")
        userinput_judge = str.isdigit(userinput)
        if userinput_judge == True:
            if  userinput == "0":
                mode = "0"
            else:
                print("請重新輸入正確選項！")
                mode = ""
        elif not userinput_judge:
            if userinput.startswith("http"):
                print(ui.start())
                os.chdir(path.wahiddl_folder())
                testcommand = command.wahiddl_FCT() + [userinput]
                subprocess.run(testcommand)
                print(ui.complete())
            elif userinput.startswith("http") == False:
                print("請重新輸入正確網址！")
            else:
                print("請重新輸入正確網址！") 
        else:
            print("請重新輸入正確命令！")
            mode = ""
    while mode == "0":
        ui.exit()
        break