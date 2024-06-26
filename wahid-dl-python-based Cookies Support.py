# wahid-dl Python-Based Cookies Support
# Version: 4.0
# Build: wahid-dl.v4.0.20240626.Python.1

# Library import
import os
import sys
import subprocess

# Download Function within OS judge
if sys.platform == "win32":
    print ("wahid-dl Python-Based Cookies Support")
    print ("------------------------------------------------------------")
    downloadlink = str (input ('請輸入欲下載影片之網址:'))
    print ("------------------------------------------------------------")
    print ("執行開始")
    print ("------------------------------------------------------------")
    os.chdir ('C:\\wahid-dl')
    subprocess.check_call ([sys.executable, '-m', 'pip', 'install', '-U', 'yt-dlp[default]'])
    downloadcommand = str (('yt-dlp --cookies-from-browser chrome -c -S"quality,res,fps,hdr:12,channels,size,br,asr" --throttled-rate 100K --merge-output-format mp4 --ffmpeg-location "C:\FFmpeg" ') + downloadlink)
    os.system (downloadcommand)
    print ("------------------------------------------------------------")
    print ("執行結束，請至資料夾內確認您的下載")
    print ("------------------------------------------------------------")
elif sys.platform == "linux":
    print ("wahid-dl Python-Based Cookies Support")
    print ("------------------------------------------------------------")
    downloadlink = str (input ('請輸入欲下載影片之網址:'))
    print ("------------------------------------------------------------")
    print ("執行開始")
    print ("------------------------------------------------------------")
    subprocess.check_call ([sys.executable, '-m', 'pip', 'install', '-U', 'yt-dlp[default]'])
    downloadcommand = str (('yt-dlp --cookies-from-browser chrome -c -S"quality,res,fps,hdr:12,channels,size,br,asr" --throttled-rate 100K --merge-output-format mp4 ') + downloadlink)
    os.system (downloadcommand)
    print ("------------------------------------------------------------")
    print ("執行結束，請至資料夾內確認您的下載")
    print ("------------------------------------------------------------")
#elif sys.platform == "darwin":
#    print ("wahid-dl Python-Based")
os.system ('pause')