import os
def uninstaller_wahiddl_ytdlp_uninstall():
    os.chdir ('C:\\wahid-dl')
    if os.path.isfile ('C:\\wahid-dl\\yt-dlp.exe') == True:
        os.remove ('C:\\wahid-dl\\yt-dlp.exe')
        print ("已刪除 yt-dlp.exe")
    elif not os.path.isfile ('C:\\wahid-dl\\yt-dlp.exe') == True:
        os.remove ('C:\\wahid-dl\\yt-dlp.exe')
        print ("不存在 yt-dlp.exe")
    else:
        print ('Internal Error')
        error_location = 'uninstaller_wahiddl_ytdlp_uninstall()'
        return error_location
def uninstaller_wahiddl_DEV_ytdlp_uninstall():
    os.chdir ('C:\\wahid-dl DEV')
    if os.path.isfile ('C:\\wahid-dl DEV\\yt-dlp.exe') == True:
        os.remove ('C:\\wahid-dl DEV\\yt-dlp.exe')
        print ("已刪除 yt-dlp.exe")
    elif not os.path.isfile ('C:\\wahid-dl DEV\\yt-dlp.exe') == True:
        os.remove ('C:\\wahid-dl DEV\\yt-dlp.exe')
        print ("不存在 yt-dlp.exe")
    else:
        print ('Internal Error')
        error_location = 'uninstaller_wahiddl_DEV_ytdlp_uninstall()'
        return error_location