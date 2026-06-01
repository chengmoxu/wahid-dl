import os
import subprocess
def install():
    os.chdir('C:\\wahid-dl\\')
    subprocess.run(['curl', '-L', '-o', 'yt-dlp.exe', 'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe'])
def update():
    os.chdir('C:\\wahid-dl\\')
    subprocess.run(['yt-dlp', '-U'])
def beta_install():
    os.chdir('C:\\wahid-dl (Beta)\\')
    subprocess.run(['curl', '-L', '-o', 'yt-dlp.exe', 'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe'])
def beta_update():
    os.chdir('C:\\wahid-dl (Beta)\\')
    subprocess.run(['yt-dlp', '-U'])