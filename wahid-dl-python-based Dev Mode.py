# wahid-dl Python-Based Dev Mode
# Version: 3.4
# Build: wahid-dl.v3.4.20240626.Python.1

# Library import
import os
import sys
import subprocess

# Download Function within OS judge
if sys.platform == "win32":
    print ("wahid-dl Python-Based Dev Mode [Windows]")
    print ("Version: 3.4")
    print ("Build: wahid-dl.v3.4.20240625.Python.1")
    print ("------------------------------------------------------------")
    commandinput = str (input ('yt-dlp命令模式，請直接輸入yt-dlp命令:'))
    print ("------------------------------------------------------------")
    os.chdir ('C:\\wahid-dl')
    subprocess.check_call ([sys.executable, '-m', 'pip', 'install', '-U', 'yt-dlp[default]'])
    command = str (('yt-dlp ') + commandinput)
    os.system (command)
elif sys.platform == "linux":
    print ("wahid-dl Python-Based Dev Mode [Linux]")
    print ("Version: 3.4")
    print ("Build: wahid-dl.v3.4.20240625.Python.1")
    print ("------------------------------------------------------------")
    commandinput = str (input ('yt-dlp命令模式，請直接輸入yt-dlp命令:'))
    print ("------------------------------------------------------------")
    subprocess.check_call ([sys.executable, '-m', 'pip', 'install', '-U', 'yt-dlp[default]'])
    command = str (('yt-dlp ') + commandinput)
    os.system (command)
#elif sys.platform == "darwin":
#    print ("macOS Mode")
os.system ('pause')