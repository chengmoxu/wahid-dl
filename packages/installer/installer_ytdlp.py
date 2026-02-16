import os
def install():
    os.chdir ('C:\\wahid-dl\\')
    os.system ('curl -L -o yt-dlp.exe https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe')
def update():
    os.chdir ('C:\\wahid-dl\\')
    os.system ('yt-dlp -U')
def beta_install():
    os.chdir ('C:\\wahid-dl (Beta)\\')
    os.system ('curl -L -o yt-dlp.exe https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe')
def beta_update():
    os.chdir ('C:\\wahid-dl (Beta)\\')
    os.system ('yt-dlp -U')