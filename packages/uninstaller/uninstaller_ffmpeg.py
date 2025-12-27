import os
from packages.core import path #unified path function
def uninstaller_ffmpeg():
    os.chdir (path.ffmpeg_folder())
    try:
        os.remove (path.ffmpeg_files()[0])
        print ("已刪除新式舊版的 ffmpeg.exe")
    except:
        print ("已不存在新式舊版 ffmpeg.exe")
    try:
        os.remove (path.ffmpeg_files()[1])
        print ("已刪除新式舊版的 ffplay.exe")
    except:
        print ("已不存在新式舊版 ffplay.exe")
    try:
        os.remove (path.ffmpeg_files()[2])
        print ("已刪除新式舊版的 ffprobe.exe")
    except:
        print ("已不存在新式舊版 ffprobe.exe")
    os.chdir (path.root())
    try:
        os.rmdir (path.ffmpeg_folder())
        print ("已刪除 FFmpeg 資料夾")
    except:
        print ("已不存在 FFmpeg 資料夾")
def uninstaller_old_ffmpeg():
    os.chdir (path.wahiddl_folder())
    try:
        os.remove (path.old_ffmpeg_files()[0])
        print ("已刪除舊式舊版的 ffmpeg.exe")
    except:
        print ("已不存在舊式舊版 ffmpeg.exe")
    try:
        os.remove (path.old_ffmpeg_files()[1])
        print ("已刪除舊式舊版的 ffplay.exe")
    except:
        print ("已不存在舊式舊版 ffplay.exe")
    try:
        os.remove (path.old_ffmpeg_files()[2])
        print ("已刪除舊式舊版的 ffprobe.exe")
    except:
        print ("已不存在舊式舊版 ffprobe.exe")