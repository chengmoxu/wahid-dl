import os
import subprocess
import re
ffmpeg_folder_name = 'FFmpeg'
def checking_ffmpeg_folder_existed():
    os.chdir ('C:\\')
    if os.path.exists (ffmpeg_folder_name):
        ffmpeg_folder_existed = True
        return ffmpeg_folder_existed
    elif not os.path.exists (ffmpeg_folder_name):
        ffmpeg_folder_existed = False
        return ffmpeg_folder_existed
def checking_ffmpeg_files_existed():
    os.chdir ('C:\\FFmpeg\\')
    if os.path.isfile ('C:\\FFmpeg\\ffmpeg.exe'):
        ffmpeg_exe_existed = True
    elif not os.path.isfile ('C:\\FFmpeg\\ffmpeg.exe'):
        ffmpeg_exe_existed = False
    if os.path.isfile ('C:\\FFmpeg\\ffplay.exe'):
        ffplay_exe_existed = True
    elif not os.path.isfile ('C:\\FFmpeg\\ffplay.exe'):
        ffplay_exe_existed = False
    if os.path.isfile ('C:\\FFmpeg\\ffprobe.exe'):
        ffprobe_exe_existed = True
    elif not os.path.isfile ('C:\\FFmpeg\\ffprobe.exe'):
        ffprobe_exe_existed = False
    return (ffmpeg_exe_existed, ffplay_exe_existed, ffprobe_exe_existed)
def checking_old_ffmpeg_files_existed():
    os.chdir ('C:\\wahid-dl\\')
    if os.path.isfile ('C:\\wahid-dl\\ffmpeg.exe'):
        ffmpeg_exe_existed = True
    elif not os.path.isfile ('C:\\wahid-dl\\ffmpeg.exe'):
        ffmpeg_exe_existed = False
    if os.path.isfile ('C:\\wahid-dl\\ffplay.exe'):
        ffplay_exe_existed = True
    elif not os.path.isfile ('C:\\wahid-dl\\ffplay.exe'):
        ffplay_exe_existed = False
    if os.path.isfile ('C:\\wahid-dl\\ffprobe.exe'):
        ffprobe_exe_existed = True
    elif not os.path.isfile ('C:\\wahid-dl\\ffprobe.exe'):
        ffprobe_exe_existed = False
    return (ffmpeg_exe_existed, ffplay_exe_existed, ffprobe_exe_existed)
def checking_ffmpeg_version():
    ffmpeg_exact_version_number = '7.1.1'
    ffmpeg_version_org_output = subprocess.getoutput ('ffmpeg -version')
    ffmpeg_version_detail = re.search(r'ffmpeg version (\d+\.\d+(?:\.\d+)?)', ffmpeg_version_org_output)
    if ffmpeg_version_detail:
        ffmpeg_check_version = str(ffmpeg_version_detail.group(1))
    if ffmpeg_check_version == ffmpeg_exact_version_number:
        print ("FFmpeg 已是v" + ffmpeg_exact_version_number + "，不需要更新")
        ffmpeg_download_need = False
        return ffmpeg_download_need
    else:
        ffmpeg_download_need = True
        return ffmpeg_download_need