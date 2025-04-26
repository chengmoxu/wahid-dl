import os
import sys
import subprocess
import shutil
import glob
import re

version_outline = "[Develop] v6.0-20250427.1-Python"

if sys.platform == "win32":
    system_os = "Windows"
elif sys.platform == "linux":
    system_os  = "Linux"
elif sys.platform == "darwin":
    system_os = "macOS"

def wahiddl_installer_without_packages():
    if os.path.exists ("C:\\wahid-dl"):
        os.chdir ("C:\\wahid-dl")
        if os.path.exists ("C:\\wahid-dl\\packages"):
            shutil.rmtree("C:\\wahid-dl\\packages")
    if not os.path.exists ("C:\\wahid-dl"):
        os.mkdir ("C:\\wahid-dl")
        os.chdir ("C:\\wahid-dl")
    os.system ("curl -L -o updates.zip https://codeload.github.com/chengmoxu/wahid-dl/zip/refs/heads/main")
    updates_folder_name = "updates"
    if not os.path.exists (updates_folder_name):
        os.mkdir (updates_folder_name)
        print (f"{updates_folder_name} 更新資料之暫存資料夾已建立")
    elif os.path.exists (updates_folder_name):
        print (f"{updates_folder_name} 更新資料之暫存資料夾已存在")
    print ("解壓縮 wahid-dl 更新資料")
    os.system ('tar -zxvf updates.zip -C "C:\\wahid-dl\\updates"')
    wahiddl_updatesfiles_folder = "C:\\wahid-dl\\updates\\wahid-dl-main\\"
    wahiddl_folder = "C:\\wahid-dl\\"
    for item in os.listdir(wahiddl_updatesfiles_folder):
        s = os.path.join(wahiddl_updatesfiles_folder, item)
        d = os.path.join(wahiddl_folder, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    shutil.rmtree("C:\\wahid-dl\\updates")
    os.remove("C:\\wahid-dl\\updates.zip")
    os.remove("C:\\wahid-dl\\.gitignore")
    os.remove("C:\\wahid-dl\\wahid-dl-colab.ipynb")
def ytdlp_installer_without_packages():
    print ("------------------------------------------------------------")
    print ("開始安裝/更新 yt-dlp")
    print ("------------------------------------------------------------")
    print ("開始下載最新版本 yt-dlp")
    os.chdir ("C:\\wahid-dl")
    yt_dlp_path = "C:\\wahid-dl\\yt-dlp.exe"
    if not os.path.exists (yt_dlp_path):
        print ("yt-dlp不存在，開始下載 yt-dlp")
        os.system ("curl -L -o yt-dlp.exe https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe")
    elif os.path.exists (yt_dlp_path):
        print ("yt-dlp已存在，開始更新 yt-dlp")
        os.system ("yt-dlp -U")
    print ("------------------------------------------------------------")
    # yt-dlp Install Checking
    os.chdir ("C:\\wahid-dl")
    if os.path.exists (yt_dlp_path):
        print ("安裝/更新 yt-dlp 完成")
    else:
        print ("安裝/更新 yt-dlp 失敗")
def ffmpeg_installer_without_packages():
    print ("------------------------------------------------------------")
    print ("開始安裝/更新 FFmpeg")
    print ("------------------------------------------------------------")
    os.chdir ("C:\\wahid-dl")
    # 移除舊有ffmpeg安裝方式之檔案
    # 移除舊式FFmpeg安裝之舊版
    if os.path.isfile ("C:\\wahid-dl\\ffmpeg.exe") == True:
        os.remove ("C:\\wahid-dl\\ffmpeg.exe")
        print ("已刪除舊式舊版的 ffmpeg.exe")
    else:
        print ("已不存在舊式舊版 ffmpeg.exe")
    if os.path.isfile ("C:\\wahid-dl\\ffplay.exe") == True:
        os.remove ("C:\\wahid-dl\\ffplay.exe")
        print ("已刪除舊式舊版的 ffplay.exe")
    else:
        print ("已不存在舊式舊版 ffplay.exe")
    if os.path.isfile ("C:\\wahid-dl\\ffprobe.exe") == True:
        os.remove ("C:\\wahid-dl\\ffprobe.exe")
        print ("已刪除舊式舊版的 ffprobe.exe")
    else:
        print ("已不存在舊式舊版 ffprobe.exe")
    # 新式FFmpeg安裝，包括系統環境變數設定
    os.chdir ("C:\\")
    # 移除新式FFmpeg安裝之舊版
    ffmpeg_folder_name = "FFmpeg"
    ffmpeg_download_need = ""
    while ffmpeg_download_need == "":
        if not os.path.exists (ffmpeg_folder_name):
            os.mkdir (ffmpeg_folder_name)
            print (f"新式 {ffmpeg_folder_name} 資料夾已建立")
            ffmpeg_download_need = "1"
        else:
            print (f"新式 {ffmpeg_folder_name} 資料夾已存在")
            # 檢查 FFmpeg 版本
            # FFmpeg Version Number，變動需要更新
            ffmpeg_exact_version_number = "7.1"
            ffmpeg_version_org_output = subprocess.getoutput ("ffmpeg -version")
            ffmpeg_version_detail = re.search(r'ffmpeg version (\d+\.\d+\.\d+)', ffmpeg_version_org_output)
            if ffmpeg_version_detail:
                ffmpeg_check_version = str(ffmpeg_version_detail.group(1))
            if ffmpeg_check_version == ffmpeg_exact_version_number:
                print ("FFmpeg 已是最新版本，不需要更新")
                ffmpeg_download_need = "0"
            else:
                # 移除新式舊版ffmpeg.exe, ffplay.exe, ffprobe.exe
                if os.path.isfile ("C:\\FFmpeg\\ffmpeg.exe") == True:
                    os.remove ("C:\\FFmpeg\\ffmpeg.exe")
                    print ("已刪除新式舊版的 ffmpeg.exe")
                else:
                    print ("已不存在新式舊版 ffmpeg.exe")
                if os.path.isfile ("C:\\FFmpeg\\ffplay.exe") == True:
                    os.remove ("C:\\FFmpeg\\ffplay.exe")
                    print ("已刪除新式舊版的 ffplay.exe")
                else:
                    print ("已不存在新式舊版 ffplay.exe")
                if os.path.isfile ("C:\\FFmpeg\\ffprobe.exe") == True:
                    os.remove ("C:\\FFmpeg\\ffprobe.exe")
                    print ("已刪除新式舊版的 ffprobe.exe")
                else:
                    print ("已不存在新式舊版 ffprobe.exe")
                ffmpeg_download_need = "1"
    while ffmpeg_download_need == "1":
        print ("開始下載最新版本 FFmpeg")
        os.chdir ("C:\\FFmpeg")
        # FFmpeg Version Number，變動需要更新
        os.system ("curl -L -o ffmpeg.zip https://github.com/GyanD/codexffmpeg/releases/download/7.1/ffmpeg-7.1-full_build.zip")
        FFmpegunzip_folder_name = "FFmpeg-unzip"
        if not os.path.exists (FFmpegunzip_folder_name):
            os.mkdir (FFmpegunzip_folder_name)
            print (f"'{FFmpegunzip_folder_name}' 資料夾已建立")
        else:
            print (f"'{FFmpegunzip_folder_name}' 資料夾已存在")
        os.system ('tar -zxvf ffmpeg.zip -C "C:\\FFmpeg\\FFmpeg-unzip"')
        # FFmpeg Version Number，變動需要更新
        ffmpeg_updatesfiles_folder = "C:\\FFmpeg\\FFmpeg-unzip\\ffmpeg-7.1-full_build\\bin\\"
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
        os.chdir ("C:\\FFmpeg\\")
        if os.path.isfile ("C:\\FFmpeg\\ffmpeg.exe") == True:
            ffmpeg_exist = "1"
        else: 
            ffmpeg_exist = "0"
        if os.path.isfile ("C:\\FFmpeg\\ffplay.exe") == True:
            ffplay_exist = "1"
        else: 
            ffplay_exist = "0"
        if os.path.isfile ("C:\\FFmpeg\\ffprobe.exe") == True:
            ffprobe_exist = "1"
        else: 
            ffprobe_exist = "0"
        if ffmpeg_exist == "1" and ffplay_exist == "1" and ffprobe_exist == "1":
            print ("安裝/更新 FFmpeg 完成")
            break
        else:
            print ("安裝/更新 FFmpeg 失敗")
            break
    while ffmpeg_download_need == "0":
        break
def wahiddl_DEV_installer_without_packages():
    if os.path.exists ("C:\\wahid-dl DEV"):
        os.chdir ("C:\\wahid-dl DEV")
        if os.path.exists ("C:\\wahid-dl DEV\\packages"):
            shutil.rmtree("C:\\wahid-dl DEV\\packages")
    if not os.path.exists ("C:\\wahid-dl DEV"):
        os.mkdir ("C:\\wahid-dl DEV")
        os.chdir ("C:\\wahid-dl DEV")
    os.system ("curl -L -o updates.zip https://codeload.github.com/chengmoxu/wahid-dl/zip/refs/heads/develop")
    updates_folder_name = "updates"
    if not os.path.exists (updates_folder_name):
        os.mkdir (updates_folder_name)
        print (f"{updates_folder_name} 更新資料之暫存資料夾已建立")
    elif os.path.exists (updates_folder_name):
        print (f"{updates_folder_name} 更新資料之暫存資料夾已存在")
    print ("解壓縮 wahid-dl DEV 更新資料")
    os.system ('tar -zxvf updates.zip -C "C:\\wahid-dl DEV\\updates"')
    wahiddl_DEV_updatesfiles_folder = "C:\\wahid-dl DEV\\updates\\wahid-dl-develop\\"
    wahiddl_DEV_folder = "C:\\wahid-dl DEV\\"
    for item in os.listdir(wahiddl_DEV_updatesfiles_folder):
        s = os.path.join(wahiddl_DEV_updatesfiles_folder, item)
        d = os.path.join(wahiddl_DEV_folder, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    shutil.rmtree("C:\\wahid-dl DEV\\updates")
    os.remove("C:\\wahid-dl DEV\\updates.zip")
    os.remove("C:\\wahid-dl DEV\\.gitignore")
    os.remove("C:\\wahid-dl DEV\\wahid-dl-colab.ipynb")
def exit():
    print ("------------------------------------------------------------")
    print ("即將結束程式")
    print ("------------------------------------------------------------")

if system_os  == "Windows":
    if not os.path.exists ("C:\\wahid-dl\\packages"):
        print ("wahid-dl Tool Without Packages [" + system_os + "]")
        print (version_outline)
        mode = ""
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
                    wahiddl_installer_without_packages()
                    ytdlp_installer_without_packages()
                    ffmpeg_installer_without_packages()
                    exit()
                    break
                elif userinput == "2":
                    wahiddl_installer_without_packages()
                    exit()
                    break
                elif userinput == "3":
                    ytdlp_installer_without_packages()
                    exit()
                    break
                elif userinput == "4":
                    ffmpeg_installer_without_packages()
                    exit()
                    break
                else:
                    print ("請重新輸入正確選項！")
            elif userinput_judge == False:
                if userinput == "DEVINSTALL":
                    wahiddl_DEV_installer_without_packages()
                    exit()
                    break
                else:
                    print ("請重新輸入正確選項！")
    elif os.path.exists ("C:\\wahid-dl\\packages"):
        from packages.core import wahiddl_tool
        wahiddl_tool.wahiddl_tool_windows_x64()
    input ()
elif system_os  == "Linux":
    if not os.path.exists ("$HOME/wahid-dl/packages"):
        print ("wahid-dl Tool Without Packages [" + system_os + "]")
        print (version_outline)
        mode = ""
        while mode == "":
            print ("Enter 'START' to start the installer")
            print ("Or enter '0' to end this program\n")
            userinput = input ("Please enter:")
            userinput_judge = str.isdigit(userinput)
            if userinput_judge == True: 
                if  userinput == "0":
                    mode = "0"
                else:
                    print ("Please re-enter the correct options!")
            elif userinput_judge == False:
                if userinput.startswith("START") == True:
                    print ("Start the installer")
                    os.system ('sudo apt install pipx')
                    os.system ('sudo apt install opus-tools')
                    os.system ('sudo apt install ffmpeg')
                    os.system ('pipx ensurepath')
                    os.system ('pipx install yt-dlp --force')
                else:
                    print ("Please re-enter the correct options!")
        while mode == "0":
            exit()
            break
    input ()
elif system_os == "macOS":
    print ("暫時不支援")
else:
    print ("不支援的平台")