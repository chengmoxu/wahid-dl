import os
def installer_wahiddl_ytdlp_install():
    os.chdir ('C:\\wahid-dl\\')
    os.system ('curl -L -o yt-dlp.exe https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe')
def installer_wahiddl_ytdlp_update():
    os.chdir ('C:\\wahid-dl\\')
    os.system ('yt-dlp -U')
def installer_wahiddl_beta_ytdlp_install():
    os.chdir ('C:\\wahid-dl (Beta)\\')
    os.system ('curl -L -o yt-dlp.exe https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe')
def installer_wahiddl_beta_ytdlp_update():
    os.chdir ('C:\\wahid-dl (Beta)\\')
    os.system ('yt-dlp -U')