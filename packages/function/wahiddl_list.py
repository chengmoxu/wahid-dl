import os
from packages.core import ui
def wahiddl_list():
    print(ui.ASCII_art())
    print(ui.ui_title_wahiddl())
    print ("------------------------------------------------------------")
    mode = ""
    while mode == "":
        print ("開始請輸入1")
        print ("或者，請輸入0結束程式\n")
        userinput = input ("請輸入：")
        userinput_judge = str.isdigit(userinput)
        if userinput_judge == True:
            if  userinput == "0":
                mode = "0"
            else:
                print ("請重新輸入正確選項！")
                mode = ""
        elif userinput == "1":
            x = 0
            for x in range (0,2,1):
                if os.path.isfile ('C:\\wahid-dl\\url_list.txt') == True:
                    print ("存在url_list.txt")
                    print ('刪除存在的url_list.txt，並自動建立新的url_list.txt，請輸入1')
                    print ('保留存在的url_list.txt，並以此清單進行下載，請輸入2')
                    choice = input ('請選擇處理方式：')
                    if choice == 1:
                        os.remove ('C:\\wahid-dl\\url_list.txt')
                        os.open('C:\\wahid-dl\\url_list.txt', os.O_RDWR|os.O_CREAT)
                        print ('請在對於url_list.txt編輯完成後再按下任一鍵以進行下載')
                        os.system ('pause')
                        break
                    elif choice == 2:
                        print ('開始讀取url_list.txt並進行下載')
                        break
                    else:
                        print ('請輸入正確的選項')
                        x = x-1
                else:
                    print ("不存在url_list.txt")
                    print ('已自動建立新的url_list.txt')
                    os.open('C:\\wahid-dl\\url_list.txt', os.O_RDWR|os.O_CREAT)
                    print ('請在對於url_list.txt編輯完成後再按下任一鍵以進行下載')
                    os.system ('pause')
                    break
            ui.ui_start()
            os.chdir ('C:\\wahid-dl')
            downloadcommand = str (('yt-dlp --batch-file url_list.txt -c -S"quality,res,fps,hdr:12,channels,size,br,asr" --throttled-rate 100K --merge-output-format mp4 --ffmpeg-location "C:\\FFmpeg"'))
            os.system (downloadcommand)
            ui.ui_complete()
        else:
            print ("請重新輸入正確命令！")
            mode = ""
    while mode == "0":
        ui.ui_exit()
        break