import os
from packages.core import path #unified path function
def uninstaller_wahiddl_ytdlp_uninstall():
    os.chdir (path.wahiddl_folder())
    if os.path.isfile (path.wahiddl_ytdlp()) == True:
        os.remove (path.wahiddl_ytdlp())
        print ("已刪除 yt-dlp.exe")
    elif not os.path.isfile (path.wahiddl_ytdlp()) == True:
        print ("不存在 yt-dlp.exe")
def uninstaller_wahiddl_DEV_ytdlp_uninstall():
    os.chdir (path.wahiddl_DEV_folder())
    if os.path.isfile (path.wahiddl_DEV_ytdlp()) == True:
        os.remove (path.wahiddl_DEV_ytdlp())
        print ("已刪除 yt-dlp.exe")
    elif not os.path.isfile (path.wahiddl_DEV_ytdlp()) == True:
        print ("不存在 yt-dlp.exe")