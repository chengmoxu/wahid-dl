# wahid-dl Python-Based for List
# [Stable] v4.6.20240816.Python.1
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

# Download Function within OS judge
if sys.platform == "win32":
    print ("wahid-dl Python-Based for List")
    print ("------------------------------------------------------------")
    mode = ""
    while mode != "0":
        print ("開始請輸入1，想要結束程式請輸入0\n")
        userinput = input ("請輸入：")
        userinput_judge = str.isdigit(userinput)
        if userinput_judge == True: 
            if  userinput == "0":
                mode = "0"
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
                print ("------------------------------------------------------------")
                print ("執行開始")
                print ("------------------------------------------------------------")
                os.chdir ('C:\\wahid-dl')
                downloadcommand = str (('yt-dlp --batch-file url_list.txt -c -S"quality,res,fps,hdr:12,channels,size,br,asr" --throttled-rate 100K --merge-output-format mp4 --ffmpeg-location "C:\\FFmpeg"'))
                os.system (downloadcommand)
                print ("------------------------------------------------------------")
                print ("執行結束，請至資料夾內確認您的下載")
                print ("------------------------------------------------------------")
            else:
               print ("請重新輸入正確選項！")
    while mode == "0":
        print("即將結束程式")
        break
elif sys.platform == "linux":
    mode = ""
    while mode != "0":
        print ("開始請輸入1，想要結束程式請輸入0\n")
        userinput = input ("請輸入：")
        userinput_judge = str.isdigit(userinput)
        if userinput_judge == True: 
            if  userinput == "0":
                mode = "0"
            elif userinput == "1":
                x = 0
                for x in range (0,2,1):
                    if os.path.isfile ('url_list.txt') == True:
                        print ("存在url_list.txt")
                        print ('刪除存在的url_list.txt，並自動建立新的url_list.txt，請輸入1')
                        print ('保留存在的url_list.txt，並以此清單進行下載，請輸入2')
                        choice = input ('請選擇處理方式：')
                        if choice == 1:
                            os.remove ('url_list.txt')
                            os.open('url_list.txt', os.O_RDWR|os.O_CREAT)
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
                        os.open('url_list.txt', os.O_RDWR|os.O_CREAT)
                        print ('請在對於url_list.txt編輯完成後再按下任一鍵以進行下載')
                        os.system ('pause')
                        break
                print ("------------------------------------------------------------")
                print ("執行開始")
                print ("------------------------------------------------------------")
                subprocess.check_call ([sys.executable, '-m', 'pip', 'install', '-U', 'yt-dlp[default]'])
                downloadcommand = str (('yt-dlp --batch-file url_list.txt -c -S"quality,res,fps,hdr:12,channels,size,br,asr" --throttled-rate 100K --merge-output-format mp4 --ffmpeg-location "C:\\FFmpeg"'))
                os.system (downloadcommand)
                print ("------------------------------------------------------------")
                print ("執行結束，請至資料夾內確認您的下載")
                print ("------------------------------------------------------------")
            else:
               print ("請重新輸入正確選項！")
    while mode == "0":
        print("即將結束程式")
        break
#elif sys.platform == "darwin":
#    print ("wahid-dl Python-Based")
os.system ('pause')