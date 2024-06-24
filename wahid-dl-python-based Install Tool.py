# wahid-dl Python-Based Install Tool
# Version: 3.4
# Build: wahid-dl.v3.4.20240624.Python.4

# Library import
import os
import sys
import subprocess
import shutil
import glob

# Install Function within OS judge
print ("wahid-dl Python-Based Install Tool")
if sys.platform == "win32":
    print ("------------------------------------------------------------")
    print ("開始執行")
    print ("------------------------------------------------------------")
    print ("建立資料夾")
    os.chdir ('C:\\')
    #os.mkdir ('wahid-dl')
    wahiddl_folder_name = 'wahid-dl'
    if not os.path.exists(wahiddl_folder_name):
        os.mkdir(wahiddl_folder_name)
        print(f"Folder '{wahiddl_folder_name}' created.")
    else:
        print(f"Folder '{wahiddl_folder_name}' already exists. This tool will remove all the old version of wahid-dl.")
        #os.system ('del *.bat')
        os.chdir ('C:\\wahid-dl')
        wahiddl_old_bat_files = glob.glob("*.bat")
        for bat_file in wahiddl_old_bat_files:
            if os.path.exists(bat_file):
                os.remove(bat_file)
                print(f"Deleted old version of {bat_file}.")
            else:
                print(f"The file {bat_file} does not exist.")
        #os.system ('del *.py')
        os.chdir ('C:\\wahid-dl')
        wahiddl_old_py_files = glob.glob("*.py")
        for py_file in wahiddl_old_py_files:
            if os.path.exists(py_file):
                os.remove(py_file)
                print(f"Deleted old version of {py_file}.")
            else:
                print(f"The file {py_file} does not exist.")
    print ("------------------------------------------------------------")
    print ("安裝 wahid-dl")
    os.chdir ('C:\\wahid-dl')
    os.system ('curl -L -o updates.zip https://codeload.github.com/chengmoxu/wahid-dl/zip/refs/heads/main')
    os.mkdir ('updates')
    os.system ('tar -zxvf updates.zip -C "C:\\wahid-dl\\updates"')
    #os.system ('move "C:\\wahid-dl\\updates\\wahid-dl-main\\*.bat" "C:\\wahid-dl\\"')
    #os.system ('move "C:\\wahid-dl\\updates\\wahid-dl-main\\*.py" "C:\\wahid-dl\\"')
    wahiddl_src_folder = "C:\\wahid-dl\\updates\\wahid-dl-main\\"
    wahiddl_dst_folder = "C:\\wahid-dl\\"
    wahiddl_bat_files = glob.glob(wahiddl_src_folder + "*.bat")
    for wahiddl_bat_file in wahiddl_bat_files:
        shutil.move(wahiddl_bat_file, wahiddl_dst_folder)
    wahiddl_py_files = glob.glob(wahiddl_src_folder + "*.py")
    for wahiddl_py_file in wahiddl_py_files:
        shutil.move(wahiddl_py_file, wahiddl_dst_folder)
    #os.system ('del "C:\\wahid-dl\\updates.zip"')
    os.remove ("C:\\wahid-dl\\updates.zip")
    #os.system ('rd /s /q "C:\\wahid-dl\\updates"')
    wahiddl_updates_folder_path = "C:\\wahid-dl\\updates"
    if os.path.exists(wahiddl_updates_folder_path):
        shutil.rmtree(wahiddl_updates_folder_path)
    else:
        print(f"Folder '{wahiddl_updates_folder_path}' does not exist.")
    print ("------------------------------------------------------------")
    print ("下載 yt-dlp")
    os.chdir ('C:\\wahid-dl')
    os.system ('curl -L -o yt-dlp.exe https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe')
    print ("------------------------------------------------------------")
    print ("下載 yt-dlp PiP Version")
    #os.system ('pip install -U "yt-dlp[default]"')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-U', 'yt-dlp[default]'])
    print ("------------------------------------------------------------")
    print ("下載 FFmpeg")
    os.chdir ('C:\\wahid-dl')
    #os.system ('del ffmpeg.exe ffplay.exe ffprobe.exe')
    wahiddl_old_ffmpeg_del = ["ffmpeg.exe", "ffplay.exe", "ffprobe.exe"]
    for file_name in wahiddl_old_ffmpeg_del:
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print(f"The old veersion {file_name} does not exist.")
    os.chdir ('C:\\')
    #os.system ('rd /s /q "C:\\FFmpeg"')
    ffmpeg_old_ver_folder_path = "C:\\FFmpeg"
    if os.path.exists(ffmpeg_old_ver_folder_path):
        shutil.rmtree(ffmpeg_old_ver_folder_path)
    else:
        print(f"Folder '{ffmpeg_old_ver_folder_path}' does not exist.")
    #os.mkdir ('FFmpeg')
    ffmpeg_folder_name = 'wahid-dl'
    if not os.path.exists(ffmpeg_folder_name):
        os.mkdir(ffmpeg_folder_name)
        print(f"Folder '{ffmpeg_folder_name}' created")
    else:
        print(f"Folder '{ffmpeg_folder_name}' already exists.")
    os.chdir ('C:\\FFmpeg')
    #os.system ('del ffmpeg.exe ffplay.exe ffprobe.exe')
    ffmpeg_old_ffmpeg_del = ["ffmpeg.exe", "ffplay.exe", "ffprobe.exe"]
    for file_name in ffmpeg_old_ffmpeg_del:
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print(f"The old veersion {file_name} does not exist.")
    os.system ('curl -L -o ffmpeg.zip https://github.com/GyanD/codexffmpeg/releases/download/7.0.1/ffmpeg-7.0.1-full_build.zip')
    os.mkdir ('FFmpeg-unzip')
    os.system ('tar -zxvf ffmpeg.zip -C "C:\\FFmpeg\\FFmpeg-unzip"')
    #os.system ('move "C:\\FFmpeg\\FFmpeg-unzip\\ffmpeg-7.0.1-full_build\\bin\\*.exe" "C:\\FFmpeg\\"')
    ffmpeg_src_folder = "C:\\FFmpeg\\FFmpeg-unzip\\ffmpeg-7.0.1-full_build\\bin\\"
    ffmpeg_dst_folder = "C:\\FFmpeg\\"
    ffmpeg_exe_files = glob.glob(ffmpeg_src_folder + "*.exe")
    for ffmpeg_exe_file in ffmpeg_exe_files:
        shutil.move(ffmpeg_exe_file, ffmpeg_dst_folder)
    os.system ('setx PATH "FFmpeg;C:\\FFmpeg\\"')
    #os.system ('del "C:\\FFmpeg\\ffmpeg.zip"')
    ffmpeg_update_del = ["ffmpeg.zip"]
    for file_name in ffmpeg_update_del:
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print(f"The update file {file_name} does not exist.")
    #os.system ('rd /s /q "C:\\FFmpeg\\ffmpeg-unzip"')
    ffmpeg_unzip_folder_path = "C:\\FFmpeg\\ffmpeg-unzip"
    if os.path.exists(ffmpeg_unzip_folder_path):
        shutil.rmtree(ffmpeg_unzip_folder_path)
    else:
        print(f"Folder '{ffmpeg_unzip_folder_path}' does not exist.")
    print ("------------------------------------------------------------")
    print ("執行完成，請至資料夾內確認安裝")
    print ("------------------------------------------------------------")
    os.system ('pause')
#elif sys.platform == "linux":
#elif sys.platform == "darwin":