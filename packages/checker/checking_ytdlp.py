import subprocess
from pathlib import Path
def checking_wahiddl_ytdlp_existed():
    try:
        wahiddl_ytdlp_path = Path('C:/wahid-dl/yt-dlp.exe')
        return wahiddl_ytdlp_path.is_file(), None     
    except Exception as error:
        return False, f"Error checking yt-dlp.exe: {str(error)}"
def checking_wahiddl_DEV_ytdlp_existed():
    try:
        wahiddl_DEV_ytdlp_path = Path('C:/wahid-dl DEV/yt-dlp.exe')
        return wahiddl_DEV_ytdlp_path.is_file(), None     
    except Exception as error:
        return False, f"Error checking yt-dlp.exe: {str(error)}"
def checking_linux_ytdlp_existed():
    try:
        result = subprocess.run(
            ["pipx", "list"], 
            capture_output=True, 
            text=True
        )
        return "yt-dlp" in result.stdout
    except:
        return False