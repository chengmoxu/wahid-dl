import os
def installer_wahiddl_ytdlp_install():
    os.chdir ('C:\\wahid-dl\\')
    os.system ('curl -L -o yt-dlp.exe https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe')
def installer_wahiddl_ytdlp_update():
    os.chdir ('C:\\wahid-dl\\')
    os.system ('yt-dlp -U')
def installer_wahiddl_DEV_ytdlp_install():
    os.chdir ('C:\\wahid-dl DEV\\')
    os.system ('curl -L -o yt-dlp.exe https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe')
def installer_wahiddl_DEV_ytdlp_update():
    os.chdir ('C:\\wahid-dl DEV\\')
    os.system ('yt-dlp -U')