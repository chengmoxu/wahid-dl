# wahid-dl Python-Based Install and Update Tool
# Version: 4.1
# Build: wahid-dl.v4.1.20240706.Python.1
'''
      ###       ###        ###         ###     ###         #######      ########             #########       ###
     ###       ###      ###   ##      ###     ###         ###          ###    ###           ###    ###      ###
    ###       ###     ###    ##      ###     ###         ###          ###    ###           ###    ###      ###
   >>>  >>>  >>>    >>>>>>>>>>>     >>>>>>>>>>>         >>>          >>>    >>>   >>>>>   >>>    >>>      >>>
  ### ##  # ###    ###      ##     ###     ###         ###          ###    ###           ###    ###      ###
 #####    ###     ###      ##     ###     ###         ###          ###    ###           ###    ###      ###
####      ##     ###      ##     ###     ###     #######          #########            #########       ###
[Stable] v4.1.20240706.Python.1

'''

# Library import
import os
import sys
import subprocess
import shutil
import glob

# Install Function within OS judge
print ("wahid-dl Python-Based Install and Update Tool")
if sys.platform == "win32":
    print ("------------------------------------------------------------")
    print ("開始執行")
    print ("------------------------------------------------------------")
    # wahid-dl 主程式安裝/更新判斷
    print ("正在確認 wahid-dl 資料夾存在與否")
    os.chdir ('C:\\')
    # 判斷wahid-dl資料夾存在與否
    #os.mkdir ('wahid-dl')
    wahiddl_folder_name = 'wahid-dl'
    if not os.path.exists (wahiddl_folder_name):
        os.mkdir (wahiddl_folder_name)
        print (f"{wahiddl_folder_name} 資料夾已建立")
    else:
        print (f"{wahiddl_folder_name} 資料夾已存在，本工具將進行更新 wahid-dl 以及附屬依賴工具")
        os.chdir ('C:\\wahid-dl')
        # 移除舊版*.bat
        #os.system ('del *.bat')
        wahiddl_old_bat_files = glob.glob ("*.bat")
        for bat_file in wahiddl_old_bat_files:
            if os.path.exists (bat_file):
                os.remove (bat_file)
                print (f"已刪除 wahid-dl 舊版的{bat_file}")
            else:
                print ("不存在 wahid-dl 舊版之 .bat 檔案")
        # 移除舊版*.py
        #os.system ('del *.py')
        os.chdir ('C:\\wahid-dl')
        wahiddl_old_py_files = glob.glob ("*.py")
        for py_file in wahiddl_old_py_files:
            if os.path.exists (py_file):
                os.remove (py_file)
                print (f"已刪除 wahid-dl 舊版的{py_file}")
            else:
                print ("不存在 wahid-dl 舊版之 .py 檔案")
    print ("------------------------------------------------------------")
    # 安裝/更新新版wahid-dl主程式
    print ("安裝/更新 wahid-dl")
    os.chdir ('C:\\wahid-dl')
    os.system ('curl -L -o updates.zip https://codeload.github.com/chengmoxu/wahid-dl/zip/refs/heads/main')
    #os.mkdir ('updates')
    updates_folder_name = 'updates'
    if not os.path.exists (updates_folder_name):
        os.mkdir (updates_folder_name)
        print (f"{updates_folder_name} 更新資料之暫存資料夾已建立")
    else:
        print (f"{updates_folder_name} 更新資料之暫存資料夾已存在")
    print ('解壓縮 wahid-dl 更新資料')
    os.system ('tar -zxvf updates.zip -C "C:\\wahid-dl\\updates"')
    #os.system ('move "C:\\wahid-dl\\updates\\wahid-dl-main\\*.bat" "C:\\wahid-dl\\"')
    #os.system ('move "C:\\wahid-dl\\updates\\wahid-dl-main\\*.py" "C:\\wahid-dl\\"')
    wahiddl_updatesfiles_folder = "C:\\wahid-dl\\updates\\wahid-dl-main\\"
    wahiddl_dst_folder = "C:\\wahid-dl\\"
    wahiddl_bat_files = glob.glob (wahiddl_updatesfiles_folder + "*.bat")
    for wahiddl_bat_file in wahiddl_bat_files:
        shutil.move (wahiddl_bat_file, wahiddl_dst_folder)
    wahiddl_py_files = glob.glob (wahiddl_updatesfiles_folder + "*.py")
    for wahiddl_py_file in wahiddl_py_files:
        shutil.move (wahiddl_py_file, wahiddl_dst_folder)
    #os.system ('del "C:\\wahid-dl\\updates.zip"')
    wahiddl_updates_file_path = "C:\\wahid-dl\\updates.zip"
    if os.path.isfile (wahiddl_updates_file_path) == True:
        os.remove (wahiddl_updates_file_path)
        print (f"更新資料 '{wahiddl_updates_file_path}' 已刪除")
    else:
        print (f"更新資料 '{wahiddl_updates_file_path}' 已不存在")
    #os.system ('rd /s /q "C:\\wahid-dl\\updates"')
    wahiddl_updates_folder_path = "C:\\wahid-dl\\updates"
    if os.path.exists (wahiddl_updates_folder_path):
        shutil.rmtree (wahiddl_updates_folder_path)
        print (f"更新資料之暫存資料夾 '{updates_folder_name}' 已刪除")
    else:
        print (f"更新資料之暫存資料夾 '{updates_folder_name}' 已不存在")
    print ("安裝/更新 wahid-dl 完成")
    print ("------------------------------------------------------------")
    print ("下載/更新 yt-dlp")
    os.chdir ('C:\\wahid-dl')
    yt_dlp_path = 'C:\\wahid-dl\\yt-dlp.exe'
    if not os.path.exists (yt_dlp_path):
        print ("yt-dlp不存在，開始下載 yt-dlp")
        os.system ('curl -L -o yt-dlp.exe https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe')
    else:
        print ("yt-dlp已存在，開始更新 yt-dlp")
        os.system ('yt-dlp -U')
    print ("下載/更新 yt-dlp 完成")
    print ("------------------------------------------------------------")
    print ("下載/更新 yt-dlp Pip Version")
    #os.system ('pip install -U "yt-dlp[default]"')
    subprocess.check_call ([sys.executable, '-m', 'pip', 'install', '-U', 'yt-dlp[default]'])
    print ("下載/更新 yt-dlp Pip Version 完成")
    print ("------------------------------------------------------------")
    print ("下載/更新 FFmpeg")
    os.chdir ('C:\\wahid-dl')
    # 移除舊有ffmpeg安裝方式之檔案
    # 移除舊式FFmpeg安裝之舊版
    #os.system ('del ffmpeg.exe ffplay.exe ffprobe.exe')
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
    #os.mkdir ('FFmpeg')
    ffmpeg_folder_name = 'FFmpeg'
    if not os.path.exists (ffmpeg_folder_name):
        os.mkdir (ffmpeg_folder_name)
        print (f"新式 {ffmpeg_folder_name} 資料夾已建立")
    else:
        print (f"新式 {ffmpeg_folder_name} 資料夾已存在")
        #os.system ('del ffmpeg.exe ffplay.exe ffprobe.exe')
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
    # 安裝/更新新版FFmpeg主程式
    os.chdir ('C:\\FFmpeg')
    os.system ('curl -L -o ffmpeg.zip https://github.com/GyanD/codexffmpeg/releases/download/7.0.1/ffmpeg-7.0.1-full_build.zip')
    #os.mkdir ('FFmpeg-unzip')
    FFmpegunzip_folder_name = 'FFmpeg-unzip'
    if not os.path.exists (FFmpegunzip_folder_name):
        os.mkdir (FFmpegunzip_folder_name)
        print (f"'{FFmpegunzip_folder_name}' 資料夾已建立")
    else:
        print (f"'{FFmpegunzip_folder_name}' 資料夾已存在")
    os.system ('tar -zxvf ffmpeg.zip -C "C:\\FFmpeg\\FFmpeg-unzip"')
    #os.system ('move "C:\\FFmpeg\\FFmpeg-unzip\\ffmpeg-7.0.1-full_build\\bin\\*.exe" "C:\\FFmpeg\\"')
    ffmpeg_updatesfiles_folder = "C:\\FFmpeg\\FFmpeg-unzip\\ffmpeg-7.0.1-full_build\\bin\\"
    ffmpeg_dst_folder = "C:\\FFmpeg\\"
    ffmpeg_exe_files = glob.glob (ffmpeg_updatesfiles_folder + "*.exe")
    for ffmpeg_exe_file in ffmpeg_exe_files:
        shutil.move (ffmpeg_exe_file, ffmpeg_dst_folder)
    # FFmpeg系統環境變數設定
    os.system ('setx PATH "FFmpeg;C:\\FFmpeg\\"')
    #os.system ('del "C:\\FFmpeg\\ffmpeg.zip"')
    ffmpeg_updates_file_path = "C:\\FFmpeg\\ffmpeg.zip"
    if os.path.isfile (ffmpeg_updates_file_path) == True:
        os.remove (ffmpeg_updates_file_path)
        print (f"更新資料 '{ffmpeg_updates_file_path}' 已刪除")
    else:
        print (f"更新資料 '{ffmpeg_updates_file_path}' 已不存在")
    #os.system ('rd /s /q "C:\\FFmpeg\\ffmpeg-unzip"')
    ffmpeg_unzip_folder_path = "C:\\FFmpeg\\ffmpeg-unzip"
    if os.path.exists (ffmpeg_unzip_folder_path):
        shutil.rmtree (ffmpeg_unzip_folder_path)
    print ("下載/更新 FFmpeg 完成")
    print ("------------------------------------------------------------")
    print ("執行完成，請至資料夾內確認安裝")
    print ("------------------------------------------------------------")
#elif sys.platform == "linux":
#elif sys.platform == "darwin":
os.system ('pause')