# wahid-dl Python-Based
# Version: 3.4
# Build: wahid-dl.v3.4.20240624.Python.2

# Library import
import os
import sys

# Download Function within OS judge
if sys.platform == "win32":
    print ("wahid-dl Python-Based [Windows Mode]")
    print ("------------------------------------------------------------")
    downloadlink = str (input ('請輸入欲下載影片之網址:'))
    print ("------------------------------------------------------------")
    print ("執行開始")
    print ("------------------------------------------------------------")
    os.system ('cd C:\\wahid-dl')
    os.system ('pip install -U "yt-dlp[default]"')
    downloadcommand = str (('yt-dlp -c -S"quality,res,fps,hdr:12,channels,size,br,asr" --throttled-rate 100K --merge-output-format mp4 ') + downloadlink)
    os.system (downloadcommand)
    os.system ('pause')
elif sys.platform == "linux":
    print ("wahid-dl Python-Based [Linux Mode]")
    print ("------------------------------------------------------------")
    downloadlink = str (input ('請輸入欲下載影片之網址:'))
    print ("------------------------------------------------------------")
    print ("執行開始")
    print ("------------------------------------------------------------")
    os.system ('pip install -U "yt-dlp[default]"')
    downloadcommand = str (('yt-dlp -c -S"quality,res,fps,hdr:12,channels,size,br,asr" --throttled-rate 100K --merge-output-format mp4 ') + downloadlink)
    os.system (downloadcommand)

#elif sys.platform == "darwin":
#    print ("macOS Mode")