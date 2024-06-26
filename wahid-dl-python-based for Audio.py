# wahid-dl Python-Based for Audio
# Version: 3.4
# Build: wahid-dl.v3.4.20240625.Python.1

# Library import
import os
import sys
import subprocess

# Download Function within OS judge
if sys.platform == "win32":
    print ("wahid-dl Python-Based for Audio")
    print ("------------------------------------------------------------")
    downloadlink = str (input ('請輸入欲下載影片之網址:'))
    print ("------------------------------------------------------------")
    print ("執行開始")
    print ("------------------------------------------------------------")
    os.chdir ('C:\\wahid-dl')
    subprocess.check_call ([sys.executable, '-m', 'pip', 'install', '-U', 'yt-dlp[default]'])
    downloadcommand = str (('yt-dlp -c --throttled-rate 100K --extract-audio -f "bestaudio[ext=m4a]" --ffmpeg-location "C:\FFmpeg" ') + downloadlink)
    os.system (downloadcommand)
    print ("------------------------------------------------------------")
    print ("執行結束，請至資料夾內確認您的下載")
    print ("------------------------------------------------------------")
elif sys.platform == "linux":
    print ("wahid-dl Python-Based for Audio")
    print ("------------------------------------------------------------")
    downloadlink = str (input ('請輸入欲下載影片之網址:'))
    print ("------------------------------------------------------------")
    print ("執行開始")
    print ("------------------------------------------------------------")
    subprocess.check_call ([sys.executable, '-m', 'pip', 'install', '-U', 'yt-dlp[default]'])
    downloadcommand = str (('yt-dlp -c --throttled-rate 100K --extract-audio -f "bestaudio[ext=m4a]" ') + downloadlink)
    os.system (downloadcommand)
    print ("------------------------------------------------------------")
    print ("執行結束，請至資料夾內確認您的下載")
    print ("------------------------------------------------------------")
#elif sys.platform == "darwin":
#    print ("wahid-dl Python-Based")
os.system ('pause')