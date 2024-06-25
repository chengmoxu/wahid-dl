# wahid-dl-python-based Format Checking Tool
# Version: 3.4
# Build: wahid-dl.v3.4.20240625.Python.1

# Library import
import os
import sys
import subprocess

# Download Function within OS judge
if sys.platform == "win32":
    print ("wahid-dl-python-based Format Checking Tool")
    print ("------------------------------------------------------------")
    testlink = str (input ('請輸入欲測試影片或音檔之網址:'))
    print ("------------------------------------------------------------")
    print ("執行開始")
    print ("------------------------------------------------------------")
    os.chdir ('C:\\wahid-dl')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-U', 'yt-dlp[default]'])
    testcommand = str (('yt-dlp -F ') + testlink)
    os.system (testcommand)
    print ("------------------------------------------------------------")
    print ("執行結束，測試結果已於上方顯示")
    print ("------------------------------------------------------------")
    os.system ('pause')
elif sys.platform == "linux":
    print ("wahid-dl-python-based Format Checking Tool")
    print ("------------------------------------------------------------")
    testlink = str (input ('請輸入欲測試影片或音檔之網址:'))
    print ("------------------------------------------------------------")
    print ("執行開始")
    print ("------------------------------------------------------------")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-U', 'yt-dlp[default]'])
    testcommand = str (('yt-dlp -F ') + testlink)
    os.system (testcommand)
    print ("------------------------------------------------------------")
    print ("執行結束，測試結果已於上方顯示")
    print ("------------------------------------------------------------")

#elif sys.platform == "darwin":
#    print ("wahid-dl Python-Based")