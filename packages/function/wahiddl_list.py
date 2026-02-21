import os
from packages.core import ui
from packages.core import path #unified path function
from packages.core import command
def main():
    print(ui.ASCII_art())
    print(ui.detail_wahiddl_list())
    mode = ""
    while mode == "":
        print(ui.divider())
        print("開始請輸入1")
        print("或者，請輸入0結束程式\n")
        userinput = input("請輸入：")
        userinput_judge = str.isdigit(userinput)
        if userinput_judge == True:
            if  userinput == "0":
                mode = "0"
            elif userinput == "1":
                x = 0
                for x in range (0,2,1):
                    if os.path.isfile (path.wahiddl_url_list()) == True:
                        print("存在url_list.txt")
                        print('刪除存在的url_list.txt，並自動建立新的url_list.txt，請輸入1')
                        print('保留存在的url_list.txt，並以此清單進行下載，請輸入2')
                        choice = input('請選擇處理方式：')
                        if choice == 1:
                            os.remove(path.wahiddl_url_list())
                            os.open(path.wahiddl_url_list(), os.O_RDWR|os.O_CREAT)
                            print('請在對於url_list.txt編輯完成後再按下任一鍵以進行下載')
                            os.system('pause')
                            break
                        elif choice == 2:
                            print('開始讀取url_list.txt並進行下載')
                            break
                        else:
                            print('請輸入正確的選項')
                            x = x-1
                    else:
                        print("不存在url_list.txt")
                        print('已自動建立新的url_list.txt')
                        os.open(path.wahiddl_url_list(), os.O_RDWR|os.O_CREAT)
                        print('請在對於url_list.txt編輯完成後再按下任一鍵以進行下載')
                        os.system('pause')
                        break
                print(ui.start())
                os.chdir(path.wahiddl_folder())
                downloadcommand = str(command.wahiddl_list())
                os.system(downloadcommand)
                print(ui.complete())
            else:
                print("請重新輸入正確選項！")
                mode = ""
        else:
            print("請重新輸入正確命令！")
            mode = ""
    while mode == "0":
        print(ui.exit())
        break