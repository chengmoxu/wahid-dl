# wahid-dl Python-Based Install Tool
# Version: 3.4
# Build: wahid-dl.v3.4.20240624.Python.2

# Library import
import os
import sys
import subprocess

# Install Function within OS judge
print ("wahid-dl Python-Based Install Tool")
if sys.platform == "win32":
    print ("------------------------------------------------------------")
    print ("開始執行")
    print ("------------------------------------------------------------")
    print ("建立資料夾")
    os.system ('cd C:\\') #待處理
    os.system ('mkdir "C:\\wahid-dl"')
    print ("------------------------------------------------------------")
    print ("安裝 wahid-dl")
    os.system ('cd C:\\wahid-dl')
    os.system ('curl -L -o updates.zip https://codeload.github.com/chengmoxu/wahid-dl/zip/refs/heads/main')
    os.system ('mkdir "C:\\wahid-dl\\updates"')
    os.system ('tar -zxvf updates.zip -C "C:\\wahid-dl\\updates"')
    os.system ('move "C:\\wahid-dl\\updates\\wahid-dl-main\\*.bat" "C:\\wahid-dl\\"')
    os.system ('move "C:\\wahid-dl\\updates\\wahid-dl-main\\*.py" "C:\\wahid-dl\\"')
    os.system ('del "C:\\wahid-dl\\updates.zip"')
    os.system ('rd /s /q "C:\\wahid-dl\\updates"')
    print ("------------------------------------------------------------")
    print ("下載 yt-dlp")
    os.system ('cd "C:\\wahid-dl"')
    os.system ('curl -L -o yt-dlp.exe https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe')
    print ("------------------------------------------------------------")
    print ("下載 FFmpeg")
    os.system ('cd "C:\\wahid-dl"')
    os.system ('del ffmpeg.exe ffplay.exe ffprobe.exe')
    os.system ('mkdir "C:\\FFmpeg"')
    os.system ('cd "C:\\FFmpeg"')
    os.system ('del ffmpeg.exe ffplay.exe ffprobe.exe')
    os.system ('curl -L -o ffmpeg.zip https://github.com/GyanD/codexffmpeg/releases/download/7.0.1/ffmpeg-7.0.1-full_build.zip')
    os.system ('mkdir "C:\\FFmpeg\\FFmpeg-unzip"')
    os.system ('tar -zxvf ffmpeg.zip -C "C:\\FFmpeg\\FFmpeg-unzip"')
    os.system ('move "C:\\FFmpeg\\FFmpeg-unzip\\ffmpeg-7.0.1-full_build\\bin\\*.exe" "C:\\FFmpeg\\"')
    os.system ('setx PATH "FFmpeg;C:\\FFmpeg\\"')
    os.system ('del "C:\\FFmpeg\\ffmpeg.zip"')
    os.system ('rd /s /q "C:\\FFmpeg\\ffmpeg-unzip"')
    print ("------------------------------------------------------------")
    print ("執行完成，請至資料夾內確認安裝")
    print ("------------------------------------------------------------")
    os.system ('pause')
#elif sys.platform == "linux":
#elif sys.platform == "darwin":