import os
import glob
import shutil
def installer_ffmpeg():
    os.chdir ('C:\\FFmpeg')
    os.system ('curl -L -o ffmpeg.zip https://github.com/GyanD/codexffmpeg/releases/download/7.1.1/ffmpeg-7.1.1-full_build.zip')
    ffmpegunzip_folder_name = 'FFmpeg-unzip'
    if not os.path.exists (ffmpegunzip_folder_name):
        os.mkdir (ffmpegunzip_folder_name)
        print (f"'{ffmpegunzip_folder_name}' 資料夾已建立")
    else:
        print (f"'{ffmpegunzip_folder_name}' 資料夾已存在")
    os.system ('tar -zxvf ffmpeg.zip -C "C:\\FFmpeg\\FFmpeg-unzip"')
    ffmpeg_updatesfiles_folder = "C:\\FFmpeg\\FFmpeg-unzip\\ffmpeg-7.1.1-full_build\\bin\\"
    ffmpeg_dst_folder = 'C:\\FFmpeg\\'
    ffmpeg_exe_files = glob.glob (ffmpeg_updatesfiles_folder + "*.exe")
    for ffmpeg_exe_file in ffmpeg_exe_files:
        shutil.move (ffmpeg_exe_file, ffmpeg_dst_folder)
    os.system ('setx PATH "FFmpeg;C:\\FFmpeg\\"')
    ffmpeg_updates_file_path = 'C:\\FFmpeg\\ffmpeg.zip'
    if os.path.isfile (ffmpeg_updates_file_path) == True:
        os.remove (ffmpeg_updates_file_path)
        print (f"更新資料 '{ffmpeg_updates_file_path}' 已刪除")
    else:
        print (f"更新資料 '{ffmpeg_updates_file_path}' 已不存在")
    if os.path.exists (ffmpegunzip_folder_name):
        shutil.rmtree (ffmpegunzip_folder_name)
        print (f"更新資料夾 '{ffmpegunzip_folder_name}' 已刪除")
    else:
        print (f"更新資料 '{ffmpegunzip_folder_name}' 已不存在")