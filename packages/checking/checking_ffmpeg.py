import os
ffmpeg_folder_name = 'FFmpeg'
def checking_ffmpeg_folder_existed():
    os.chdir ('C:\\')
    if os.path.exists (ffmpeg_folder_name):
        ffmpeg_folder_existed = 'True'
        return ffmpeg_folder_existed
    elif not os.path.exists (ffmpeg_folder_name):
        ffmpeg_folder_existed = 'Flase'
        return ffmpeg_folder_existed
    else:
        ffmpeg_folder_existed = 'Internal Error'
        error_location = 'checking_ffmpeg_folder_existed()'
        return ffmpeg_folder_existed, error_location
def checking_ffmpeg_files_existed():
    os.chdir ('C:\\FFmpeg\\')
    if os.path.isfile ('C:\\wahid-dl\\ffmpeg.exe'):
        ffmpeg_exe_existed = 'True'
        error_location = 'False'
    elif not os.path.isfile ('C:\\wahid-dl\\ffmpeg.exe'):
        ffmpeg_exe_existed = 'False'
        error_location = 'False'
    else:
        ffmpeg_exe_existed = 'Internal Error'
        error_location = 'checking_ffmpeg_files_existed()'
    if os.path.isfile ('C:\\wahid-dl\\ffplay.exe'):
        ffplay_exe_existed = 'True'
        error_location = 'False'
    elif not os.path.isfile ('C:\\wahid-dl\\ffplay.exe'):
        ffplay_exe_existed = 'False'
        error_location = 'False'
    else:
        ffplay_exe_existed = 'Internal Error'
        error_location = 'checking_ffmpeg_files_existed()'
    if os.path.isfile ('C:\\wahid-dl\\ffprobe.exe'):
        ffprobe_exe_existed = 'True'
        error_location = 'False'
    elif not os.path.isfile ('C:\\wahid-dl\\ffprobe.exe'):
        ffprobe_exe_existed = 'False'
        error_location = 'False'
    else:
        ffprobe_exe_existed = 'Internal Error'
        error_location = 'checking_ffmpeg_files_existed()'
    return ffmpeg_exe_existed, ffplay_exe_existed, ffprobe_exe_existed, error_location