from pathlib import Path
def ytdlp():
    try:
        wahiddl_ytdlp_path = Path("C:\\wahid-dl\\yt-dlp.exe")
        return wahiddl_ytdlp_path.is_file()
    except Exception:
        return False
def beta_ytdlp():
    try:
        wahiddl_beta_ytdlp_path = Path("C:\\wahid-dl (Beta)\\yt-dlp.exe")
        return wahiddl_beta_ytdlp_path.is_file()
    except Exception:
        return False