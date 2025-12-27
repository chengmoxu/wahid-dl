import os
from packages.core import path #unified path function
def uninstaller_wahiddl_ytdlp_uninstall():
    try:
        os.remove (path.wahiddl_ytdlp())
        print ("已刪除 yt-dlp.exe")
    except:
        print ("不存在 yt-dlp.exe")
def uninstaller_wahiddl_DEV_ytdlp_uninstall():
    try:
        os.remove (path.wahiddl_DEV_ytdlp())
        print ("已刪除 yt-dlp.exe")
    except:
        print ("不存在 yt-dlp.exe")