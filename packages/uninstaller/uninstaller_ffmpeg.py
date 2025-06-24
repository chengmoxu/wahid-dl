import os
def uninstaller_ffmpeg():
    os.chdir ('C:\\FFmpeg')
    if os.path.isfile ('C:\\FFmpeg\\ffmpeg.exe') == True:
        os.remove ('C:\\FFmpeg\\ffmpeg.exe')
        print ("已刪除新式舊版的 ffmpeg.exe")
    elif not os.path.isfile ('C:\\FFmpeg\\ffmpeg.exe') == True:
        print ("已不存在新式舊版 ffmpeg.exe")
    if os.path.isfile ('C:\\FFmpeg\\ffplay.exe') == True:
        os.remove ('C:\\FFmpeg\\ffplay.exe')
        print ("已刪除新式舊版的 ffplay.exe")
    elif not os.path.isfile ('C:\\FFmpeg\\ffplay.exe') == True:
        print ("已不存在新式舊版 ffplay.exe")
    if os.path.isfile ('C:\\FFmpeg\\ffprobe.exe') == True:
        os.remove ('C:\\FFmpeg\\ffprobe.exe')
        print ("已刪除新式舊版的 ffprobe.exe")
    if os.path ('C:\\FFmpeg') == True:
        os.rmdir ('C:\\FFmpeg')
        print ("已刪除FFmpeg資料夾")
    elif not os.path.isfile ('C:\\FFmpeg\\ffprobe.exe') == True:
        print ("已不存在新式舊版 ffprobe.exe")
def uninstaller_old_ffmpeg():
    os.chdir ('C:\\wahid-dl')
    if os.path.isfile ('C:\\wahid-dl\\ffmpeg.exe') == True:
        os.remove ('C:\\wahid-dl\\ffmpeg.exe')
        print ("已刪除舊式舊版的 ffmpeg.exe")
    elif not os.path.isfile ('C:\\wahid-dl\\ffmpeg.exe') == True:
        print ("已不存在舊式舊版 ffmpeg.exe")
    if os.path.isfile ('C:\\wahid-dl\\ffplay.exe') == True:
        os.remove ('C:\\wahid-dl\\ffplay.exe')
        print ("已刪除舊式舊版的 ffplay.exe")
    elif not os.path.isfile ('C:\\wahid-dl\\ffplay.exe') == True:
        print ("已不存在舊式舊版 ffplay.exe")
    if os.path.isfile ('C:\\wahid-dl\\ffprobe.exe') == True:
        os.remove ('C:\\wahid-dl\\ffprobe.exe')
        print ("已刪除舊式舊版的 ffprobe.exe")
    elif not os.path.isfile ('C:\\wahid-dl\\ffprobe.exe') == True:
        print ("已不存在舊式舊版 ffprobe.exe")