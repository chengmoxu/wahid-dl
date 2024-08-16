# wahid-dl Python-Based Install and Update Tool
# [DEV] v4.5.20240816.Python.1
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
import shutil
import glob
import re

# Install/Update Function within OS judge
print ("wahid-dl Python-Based Install and Update Tool")
if sys.platform == "win32":
    def wahiddl_installer():
        print ("------------------------------------------------------------")
        print ("開始安裝/更新wahid-dl主程式")
        print ("------------------------------------------------------------")
        # wahid-dl 主程式安裝/更新判斷
        print ("正在確認 wahid-dl 資料夾存在與否")
        os.chdir ('C:\\')
        wahiddl_folder_name = 'wahid-dl'
        if not os.path.exists (wahiddl_folder_name):
            os.mkdir (wahiddl_folder_name)
            print (f"{wahiddl_folder_name} 資料夾已建立")
        else:
            print (f"{wahiddl_folder_name} 資料夾已存在，本工具將進行更新 wahid-dl")
            os.chdir ('C:\\wahid-dl')
            # 移除舊版*.bat
            wahiddl_old_bat_files = glob.glob ("*.bat")
            for bat_file in wahiddl_old_bat_files:
                if os.path.exists (bat_file):
                    os.remove (bat_file)
                    print (f"已刪除 wahid-dl 舊版的{bat_file}")
                else:
                    print ("不存在 wahid-dl 舊版之 .bat 檔案")
            # 移除舊版*.py
            os.chdir ('C:\\wahid-dl')
            wahiddl_old_py_files = glob.glob ("*.py")
            for py_file in wahiddl_old_py_files:
                if os.path.exists (py_file):
                    os.remove (py_file)
                    print (f"已刪除 wahid-dl 舊版的{py_file}")
                else:
                    print ("不存在 wahid-dl 舊版之 .py 檔案")
        print ("------------------------------------------------------------")
        print ("開始下載最新版本 wahid-dl 主程式")
        os.chdir ('C:\\wahid-dl')
        os.system ('curl -L -o updates.zip https://codeload.github.com/chengmoxu/wahid-dl/zip/refs/heads/main')
        updates_folder_name = 'updates'
        if not os.path.exists (updates_folder_name):
            os.mkdir (updates_folder_name)
            print (f"{updates_folder_name} 更新資料之暫存資料夾已建立")
        else:
            print (f"{updates_folder_name} 更新資料之暫存資料夾已存在")
        print ('解壓縮 wahid-dl 更新資料')
        os.system ('tar -zxvf updates.zip -C "C:\\wahid-dl\\updates"')
        wahiddl_updatesfiles_folder = "C:\\wahid-dl\\updates\\wahid-dl-main\\"
        wahiddl_dst_folder = "C:\\wahid-dl\\"
        wahiddl_bat_files = glob.glob (wahiddl_updatesfiles_folder + "*.bat")
        for wahiddl_bat_file in wahiddl_bat_files:
            shutil.move (wahiddl_bat_file, wahiddl_dst_folder)
        wahiddl_py_files = glob.glob (wahiddl_updatesfiles_folder + "*.py")
        for wahiddl_py_file in wahiddl_py_files:
            shutil.move (wahiddl_py_file, wahiddl_dst_folder)
        wahiddl_updates_file_path = "C:\\wahid-dl\\updates.zip"
        if os.path.isfile (wahiddl_updates_file_path) == True:
            os.remove (wahiddl_updates_file_path)
            print (f"更新資料 '{wahiddl_updates_file_path}' 已刪除")
        else:
            print (f"更新資料 '{wahiddl_updates_file_path}' 已不存在")
        wahiddl_updates_folder_path = "C:\\wahid-dl\\updates"
        if os.path.exists (wahiddl_updates_folder_path):
            shutil.rmtree (wahiddl_updates_folder_path)
            print (f"更新資料之暫存資料夾 '{updates_folder_name}' 已刪除")
        else:
            print (f"更新資料之暫存資料夾 '{updates_folder_name}' 已不存在")
        print ("------------------------------------------------------------")
        # wahid-dl Installation Check
        os.chdir ('C:\\')
        wahiddl_folder_name = 'wahid-dl'
        if os.path.exists (wahiddl_folder_name):
            os.chdir ('C:\\wahid-dl')
            wahiddl_py_files = glob.glob ("*.py")
            for py_file in wahiddl_py_files:
                if os.path.exists (py_file):
                    wahiddl_py_insatll_checking = '1'
                else:
                    wahiddl_py_insatll_checking = '0'
            wahiddl_bat_files = glob.glob ("*.bat")
            for bat_file in wahiddl_bat_files:
                if os.path.exists (bat_file):
                    wahiddl_bat_insatll_checking = '1'
                else:
                    wahiddl_bat_insatll_checking = '0'
            if wahiddl_py_insatll_checking == '1' and wahiddl_bat_insatll_checking == '1':
                print ("安裝/更新 wahid-dl 完成")
            else:
                print ("安裝/更新 wahid-dl 失敗")
        else:
            print ("安裝/更新 wahid-dl 失敗")
    def ytdlp_intstaller():
        print ("------------------------------------------------------------")
        print ("開始安裝/更新 yt-dlp")
        print ("------------------------------------------------------------")
        print ("開始下載最新版本 yt-dlp")
        os.chdir ('C:\\wahid-dl')
        yt_dlp_path = 'C:\\wahid-dl\\yt-dlp.exe'
        if not os.path.exists (yt_dlp_path):
            print ("yt-dlp不存在，開始下載 yt-dlp")
            os.system ('curl -L -o yt-dlp.exe https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe')
        else:
            print ("yt-dlp已存在，開始更新 yt-dlp")
            os.system ('yt-dlp -U')
        print ("------------------------------------------------------------")
        # yt-dlp Install Checking
        os.chdir ('C:\\wahid-dl')
        if os.path.exists (yt_dlp_path):
            print ("安裝/更新 yt-dlp 完成")
        else:
            print ("安裝/更新 yt-dlp 失敗")
        print ("------------------------------------------------------------")
        print ("開始下載最新版本 yt-dlp Pip Version")
        subprocess.check_call ([sys.executable, '-m', 'pip', 'install', '-U', 'yt-dlp[default]'])
        print ("安裝/更新 yt-dlp Pip Version 完成")
    def ffmpeg_installer():
        print ("------------------------------------------------------------")
        print ("開始安裝/更新 FFmpeg")
        print ("------------------------------------------------------------")
        os.chdir ('C:\\wahid-dl')
        # 移除舊有ffmpeg安裝方式之檔案
        # 移除舊式FFmpeg安裝之舊版
        if os.path.isfile ('C:\\wahid-dl\\ffmpeg.exe') == True:
            os.remove ('C:\\wahid-dl\\ffmpeg.exe')
            print ("已刪除舊式舊版的 ffmpeg.exe")
        else:
            print ("已不存在舊式舊版 ffmpeg.exe")
        if os.path.isfile ('C:\\wahid-dl\\ffplay.exe') == True:
            os.remove ('C:\\wahid-dl\\ffplay.exe')
            print ("已刪除舊式舊版的 ffplay.exe")
        else:
            print ("已不存在舊式舊版 ffplay.exe")
        if os.path.isfile ('C:\\wahid-dl\\ffprobe.exe') == True:
            os.remove ('C:\\wahid-dl\\ffprobe.exe')
            print ("已刪除舊式舊版的 ffprobe.exe")
        else:
            print ("已不存在舊式舊版 ffprobe.exe")
        # 新式FFmpeg安裝，包括系統環境變數設定
        os.chdir ('C:\\')
        # 移除新式FFmpeg安裝之舊版
        ffmpeg_old_ver_folder_path = "C:\\FFmpeg"
        ffmpeg_folder_name = 'FFmpeg'
        ffmpeg_download_need = ''
        while ffmpeg_download_need == '':
            if not os.path.exists (ffmpeg_folder_name):
                os.mkdir (ffmpeg_folder_name)
                print (f"新式 {ffmpeg_folder_name} 資料夾已建立")
                ffmpeg_download_need = '1'
            else:
                print (f"新式 {ffmpeg_folder_name} 資料夾已存在")
                # 檢查 FFmpeg 版本
                # FFmpeg Version Number，變動需要更新
                ffmpeg_exact_version_number = '7.0.2'
                ffmpeg_version_org_output = subprocess.getoutput ('ffmpeg -version')
                ffmpeg_version_detail = re.search(r'ffmpeg version (\d+\.\d+\.\d+)', ffmpeg_version_org_output)
                if ffmpeg_version_detail:
                    ffmpeg_check_version = str(ffmpeg_version_detail.group(1))
                if ffmpeg_check_version == ffmpeg_exact_version_number:
                    print ("FFmpeg 已是最新版本，不需要更新")
                    ffmpeg_download_need = '0'
                else:
                    # 移除新式舊版ffmpeg.exe, ffplay.exe, ffprobe.exe
                    if os.path.isfile ('C:\\FFmpeg\\ffmpeg.exe') == True:
                        os.remove ('C:\\FFmpeg\\ffmpeg.exe')
                        print ("已刪除新式舊版的 ffmpeg.exe")
                    else:
                        print ("已不存在新式舊版 ffmpeg.exe")
                    if os.path.isfile ('C:\\FFmpeg\\ffplay.exe') == True:
                        os.remove ('C:\\FFmpeg\\ffplay.exe')
                        print ("已刪除新式舊版的 ffplay.exe")
                    else:
                        print ("已不存在新式舊版 ffplay.exe")
                    if os.path.isfile ('C:\\FFmpeg\\ffprobe.exe') == True:
                        os.remove ('C:\\FFmpeg\\ffprobe.exe')
                        print ("已刪除新式舊版的 ffprobe.exe")
                    else:
                        print ("已不存在新式舊版 ffprobe.exe")
                    ffmpeg_download_need = '1'
        while ffmpeg_download_need == '1':
            print ("開始下載最新版本 FFmpeg")
            os.chdir ('C:\\FFmpeg')
            # FFmpeg Version Number，變動需要更新
            os.system ('curl -L -o ffmpeg.zip https://github.com/GyanD/codexffmpeg/releases/download/7.0.2/ffmpeg-7.0.2-full_build.zip')
            FFmpegunzip_folder_name = 'FFmpeg-unzip'
            if not os.path.exists (FFmpegunzip_folder_name):
                os.mkdir (FFmpegunzip_folder_name)
                print (f"'{FFmpegunzip_folder_name}' 資料夾已建立")
            else:
                print (f"'{FFmpegunzip_folder_name}' 資料夾已存在")
            os.system ('tar -zxvf ffmpeg.zip -C "C:\\FFmpeg\\FFmpeg-unzip"')
            # FFmpeg Version Number，變動需要更新
            ffmpeg_updatesfiles_folder = "C:\\FFmpeg\\FFmpeg-unzip\\ffmpeg-7.0.2-full_build\\bin\\"
            ffmpeg_dst_folder = "C:\\FFmpeg\\"
            ffmpeg_exe_files = glob.glob (ffmpeg_updatesfiles_folder + "*.exe")
            for ffmpeg_exe_file in ffmpeg_exe_files:
                shutil.move (ffmpeg_exe_file, ffmpeg_dst_folder)
            # FFmpeg系統環境變數設定
            os.system ('setx PATH "FFmpeg;C:\\FFmpeg\\"')
            ffmpeg_updates_file_path = "C:\\FFmpeg\\ffmpeg.zip"
            if os.path.isfile (ffmpeg_updates_file_path) == True:
                os.remove (ffmpeg_updates_file_path)
                print (f"更新資料 '{ffmpeg_updates_file_path}' 已刪除")
            else:
                print (f"更新資料 '{ffmpeg_updates_file_path}' 已不存在")
            ffmpeg_unzip_folder_path = "C:\\FFmpeg\\ffmpeg-unzip"
            if os.path.exists (ffmpeg_unzip_folder_path):
                shutil.rmtree (ffmpeg_unzip_folder_path)
            print ("------------------------------------------------------------")
            # FFmpeg Installation Check
            os.chdir ('C:\\FFmpeg\\')
            if os.path.isfile ('C:\\FFmpeg\\ffmpeg.exe') == True:
                ffmpeg_exist = '1'
            else: 
                ffmpeg_exist = '0'
            if os.path.isfile ('C:\\FFmpeg\\ffplay.exe') == True:
                ffplay_exist = '1'
            else: 
                ffplay_exist = '0'
            if os.path.isfile ('C:\\FFmpeg\\ffprobe.exe') == True:
                ffprobe_exist = '1'
            else: 
                ffprobe_exist = '0'
            if ffmpeg_exist == '1' and ffplay_exist == '1' and ffprobe_exist == '1':
                print ("安裝/更新 FFmpeg 完成")
            else:
                print ("安裝/更新 FFmpeg 失敗")
        while ffmpeg_download_need == '0':
            break
    def wahiddl_DEV_installer():
        print ("------------------------------------------------------------")
        print ("開始安裝/更新wahid-dl DEV主程式")
        print ("------------------------------------------------------------")
        # wahid-dl DEV 主程式安裝/更新判斷
        print ("正在確認 wahid-dl DEV 資料夾存在與否")
        os.chdir ('C:\\')
        wahiddl_folder_name = 'wahid-dl DEV'
        if not os.path.exists (wahiddl_folder_name):
            os.mkdir (wahiddl_folder_name)
            print (f"{wahiddl_folder_name} 資料夾已建立")
        else:
            print (f"{wahiddl_folder_name} 資料夾已存在，本工具將進行更新 wahid-dl DEV")
            os.chdir ('C:\\wahid-dl DEV')
            # 移除舊版*.bat
            wahiddl_old_bat_files = glob.glob ("*.bat")
            for bat_file in wahiddl_old_bat_files:
                if os.path.exists (bat_file):
                    os.remove (bat_file)
                    print (f"已刪除 wahid-dl DEV 舊版的{bat_file}")
                else:
                    print ("不存在 wahid-dl DEV 舊版之 .bat 檔案")
            # 移除舊版*.py
            os.chdir ('C:\\wahid-dl')
            wahiddl_old_py_files = glob.glob ("*.py")
            for py_file in wahiddl_old_py_files:
                if os.path.exists (py_file):
                    os.remove (py_file)
                    print (f"已刪除 wahid-dl DEV 舊版的{py_file}")
                else:
                    print ("不存在 wahid-dl DEV 舊版之 .py 檔案")
        print ("------------------------------------------------------------")
        # 安裝/更新新版wahid-dl DEV 主程式
        print ("安裝/更新 wahid-dl DEV")
        os.chdir ('C:\\wahid-dl DEV')
        os.system ('curl -L -o updates.zip https://codeload.github.com/chengmoxu/wahid-dl/zip/refs/heads/develop')
        updates_folder_name = 'updates'
        if not os.path.exists (updates_folder_name):
            os.mkdir (updates_folder_name)
            print (f"{updates_folder_name} 更新資料之暫存資料夾已建立")
        else:
            print (f"{updates_folder_name} 更新資料之暫存資料夾已存在")
        print ('解壓縮 wahid-dl DEV 更新資料')
        os.system ('tar -zxvf updates.zip -C "C:\\wahid-dl DEV\\updates"')
        wahiddl_updatesfiles_folder = "C:\\wahid-dl DEV\\updates\\wahid-dl-develop\\"
        wahiddl_dst_folder = "C:\\wahid-dl DEV\\"
        wahiddl_bat_files = glob.glob (wahiddl_updatesfiles_folder + "*.bat")
        for wahiddl_bat_file in wahiddl_bat_files:
            shutil.move (wahiddl_bat_file, wahiddl_dst_folder)
        wahiddl_py_files = glob.glob (wahiddl_updatesfiles_folder + "*.py")
        for wahiddl_py_file in wahiddl_py_files:
            shutil.move (wahiddl_py_file, wahiddl_dst_folder)
        wahiddl_updates_file_path = "C:\\wahid-dl DEV\\updates.zip"
        if os.path.isfile (wahiddl_updates_file_path) == True:
            os.remove (wahiddl_updates_file_path)
            print (f"更新資料 '{wahiddl_updates_file_path}' 已刪除")
        else:
            print (f"更新資料 '{wahiddl_updates_file_path}' 已不存在")
        wahiddl_updates_folder_path = "C:\\wahid-dl DEV\\updates"
        if os.path.exists (wahiddl_updates_folder_path):
            shutil.rmtree (wahiddl_updates_folder_path)
            print (f"更新資料之暫存資料夾 '{updates_folder_name}' 已刪除")
        else:
            print (f"更新資料之暫存資料夾 '{updates_folder_name}' 已不存在")
        print ("------------------------------------------------------------")
        # wahid-dl DEV Installation Check
        os.chdir ('C:\\')
        wahiddl_DEV_folder_name = 'wahid-dl DEV'
        if os.path.exists (wahiddl_DEV_folder_name):
            os.chdir ('C:\\wahid-dl DEV')
            wahiddl_DEV_py_files = glob.glob ("*.py")
            for DEV_py_file in wahiddl_DEV_py_files:
                if os.path.exists (DEV_py_file):
                    wahiddl_DEV_py_insatll_checking = '1'
                else:
                    wahiddl_DEV_py_insatll_checking = '0'
            wahiddl_DEV_bat_files = glob.glob ("*.bat")
            for DEV_bat_file in wahiddl_DEV_bat_files:
                if os.path.exists (DEV_bat_file):
                    wahiddl_DEV_bat_insatll_checking = '1'
                else:
                    wahiddl_DEV_bat_insatll_checking = '0'
            if wahiddl_DEV_py_insatll_checking == '1' and wahiddl_DEV_bat_insatll_checking == '1':
                print ("安裝/更新 wahid-dl DEV 完成")
            else:
                print ("安裝/更新 wahid-dl DEV 失敗")
        else:
            print ("安裝/更新 wahid-dl DEV 失敗")
    def exit():
        print ("------------------------------------------------------------")
        print ("即將結束程式")
        print ("------------------------------------------------------------")
    mode = ""
    mode_con = ""
    while mode == "":
        print ("1: 完整安裝/更新 wahid-dl 及附屬依賴工具")
        print ("2: 更新 wahid-dl 主程式")
        print ("3: 更新 yt-dlp")
        print ("4: 更新 FFmpeg")
        print ("DEVINSTALL: 安裝/更新 wahid-dl Dev 主程式")
        print ("0: 離開程式")
        userinput = input ("請選擇執行項目: ")
        userinput_judge = str.isdigit(userinput)
        if userinput_judge == True: 
            if userinput == "0":
                exit()
                break
            elif userinput == "1":
                print ("完整安裝/更新 wahid-dl 及附屬依賴工具")
                wahiddl_installer()
                ytdlp_intstaller()
                ffmpeg_installer()
                exit()
                break
            elif userinput == "2":
                wahiddl_installer()
                exit()
                break
            elif userinput == "3":
                ytdlp_intstaller()
                exit()
                break
            elif userinput == "4":
                ffmpeg_installer()
                exit()
                break
            else:
                print ("請重新輸入正確選項！")
        elif userinput_judge == False:
            if userinput == "DEVINSTALL":
                wahiddl_DEV_installer()
                exit()
                break
#elif sys.platform == "linux":
#elif sys.platform == "darwin":
os.system ('pause')