# wahid-dl Python-Based
# Version: 3.4
# Build: wahid-dl.v3.4.20240624.Python.1

# Library import
import os
import sys
import subprocess

# OS judge
if sys.platform == "win32":
    print ("wahid-dl Python-Based [Windows Mode]")
    print ("------------------------------------------------------------")
    downloadlink = str (input (r'請輸入欲下載影片之網址:'))
    print ("------------------------------------------------------------")
    print ("執行開始")
    print ("------------------------------------------------------------")
    os.system (r'cd C:\wahid-dl') # 使用r"字串"以避免反斜線被視為跳脫字元之情形
    subprocess.getoutput ('pip install -U "yt-dlp[default]"')
    downloadcommand = str (('yt-dlp -c -S"quality,res,fps,hdr:12,channels,size,br,asr" --throttled-rate 100K --merge-output-format mp4 ') + downloadlink)
    subprocess.getoutput (downloadcommand)
    os.system ('pause')
#elif sys.platform == "linux":
#    print ("Linux Mode")
#elif sys.platform == "darwin":
#    print ("macOS Mode")