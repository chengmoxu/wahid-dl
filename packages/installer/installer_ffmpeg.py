import os
import glob
import shutil
import subprocess
from packages.core import path #unified path function
from packages.core import url #unified url function
def v2(): #v2.20260520.2
    os.chdir(path.ffmpeg_folder())
    subprocess.run(['curl', '-L', '-o', 'ffmpeg.zip', url.ffmpeg()])
    try:
        os.mkdir(path.ffmpeg_update_unzip_folder())
        print("更新資料夾已建立")
    except:
        print("更新資料夾已存在")
        if os.path.exists(path.ffmpeg_update_file()):
            os.remove(path.ffmpeg_update_file())
    subprocess.run(['tar', '-zxvf', 'ffmpeg.zip', '-C', path.ffmpeg_update_unzip_folder()])
    ffmpeg_exe_files = glob.glob(path.ffmpeg_update_unzip_folder() + "ffmpeg-8.1.1-full_build\\bin\\" + "*.exe")
    for ffmpeg_exe_file in ffmpeg_exe_files:
        shutil.move (ffmpeg_exe_file, path.ffmpeg_folder())
    try:
        os.remove(path.ffmpeg_update_file())
        print(f"更新資料 '{path.ffmpeg_update_file()}' 已刪除")
    except:
        print(f"更新資料 '{path.ffmpeg_update_file()}' 已不存在")
    try:
        shutil.rmtree(path.ffmpeg_update_unzip_folder())
        print("更新資料夾已刪除")
    except:
        print("更新資料夾已不存在")