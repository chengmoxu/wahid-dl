import os
import glob
import shutil
from packages.core import path #unified path function
from packages.core import url #unified url function
def installer_ffmpeg():
    os.chdir (path.ffmpeg_folder())
    os.system ('curl -L -o ffmpeg.zip ' + url.ffmpeg())
    ffmpegunzip_folder_name = 'FFmpeg-unzip'
    try:
        os.mkdir (ffmpegunzip_folder_name)
        print (f"'{ffmpegunzip_folder_name}' 資料夾已建立")
    except:
        print (f"'{ffmpegunzip_folder_name}' 資料夾已存在")
    os.system ('tar -zxvf ffmpeg.zip -C "C:\\FFmpeg\\FFmpeg-unzip"')
    ffmpeg_updatesfiles_folder = "C:\\FFmpeg\\FFmpeg-unzip\\ffmpeg-8.0.1-full_build\\bin\\"
    ffmpeg_dst_folder = path.ffmpeg_folder()
    ffmpeg_exe_files = glob.glob (ffmpeg_updatesfiles_folder + "*.exe")
    for ffmpeg_exe_file in ffmpeg_exe_files:
        shutil.move (ffmpeg_exe_file, ffmpeg_dst_folder)
    #os.system ('setx PATH "FFmpeg;C:\\FFmpeg\\"') 
    #NOTICE: A severe flaw exists that could potentially lead to the removal of all system environment variables.
    ffmpeg_updates_file_path = 'C:\\FFmpeg\\ffmpeg.zip'
    try:
        os.remove (ffmpeg_updates_file_path)
        print (f"更新資料 '{ffmpeg_updates_file_path}' 已刪除")
    except:
        print (f"更新資料 '{ffmpeg_updates_file_path}' 已不存在")
    try:
        shutil.rmtree (ffmpegunzip_folder_name)
        print (f"更新資料夾 '{ffmpegunzip_folder_name}' 已刪除")
    except:
        print (f"更新資料 '{ffmpegunzip_folder_name}' 已不存在")