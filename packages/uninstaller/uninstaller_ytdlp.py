import os
from packages.core import path #unified path function
def uninstall():
    try:
        os.remove (path.wahiddl_ytdlp())
        print ("已刪除 yt-dlp.exe")
    except:
        print ("不存在 yt-dlp.exe")
def beta_uninstall():
    try:
        os.remove (path.wahiddl_beta_ytdlp())
        print ("已刪除 yt-dlp.exe")
    except:
        print ("不存在 yt-dlp.exe")