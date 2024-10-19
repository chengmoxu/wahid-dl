import os
def checking_wahiddl_ytdlp_file_existed():
    os.chdir ('C:\\wahid-dl\\')
    if os.path.isfile ('C:\\wahid-dl\\yt-dlp.exe'):
        ytdlp_exe_existed = True
        error_location = False
    elif not os.path.isfile ('C:\\wahid-dl\\yt-dlp.exe'):
        ytdlp_exe_existed = False
        error_location = False
    else:
        ytdlp_exe_existed = 'Internal Error'
        error_location = 'checking_wahiddl_ytdlp_file_existed()'
    return ytdlp_exe_existed, error_location
def checking_wahiddl_DEV_ytdlp_file_existed():
    os.chdir ('C:\\wahid-dl DEV\\')
    if os.path.isfile ('C:\\wahid-dl DEV\\yt-dlp.exe'):
        ytdlp_exe_existed = True
        error_location = False
    elif not os.path.isfile ('C:\\wahid-dl DEV\\yt-dlp.exe'):
        ytdlp_exe_existed = False
        error_location = False
    else:
        ytdlp_exe_existed = 'Internal Error'
        error_location = 'checking_wahiddl_DEV_ytdlp_file_existed()'
    return ytdlp_exe_existed, error_location