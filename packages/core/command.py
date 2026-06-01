from packages.core import path
def wahiddl():
    return['yt-dlp', '-c', '-S', 'quality,res,fps,hdr:12,channels,size,br,asr', '--throttled-rate', '100K', '--merge-output-format', 'mp4', '--ffmpeg-location', path.ffmpeg_folder()]
def wahiddl_FCT():
    return['yt-dlp', '-F']
def wahiddl_subtitle():
    return['yt-dlp', '--list-subs', 'yt-dlp', '-c', '--sub-lang', '--write-subs', '--skip-download']
def wahiddl_QS():
    return['yt-dlp', '-F', 'yt-dlp', '-c', '-f', '+bestaudio[ext=m4a]', '--throttled-rate', '100K', '--merge-output-format', 'mp4', '--ffmpeg-location', path.ffmpeg_folder()]
def wahiddl_live():
    return['yt-dlp', '-c', '--live-from-start', '-S', 'quality,res,fps,hdr:12,channels,size,br,asr', '--throttled-rate', '100K', '--merge-output-format', 'mp4', '--ffmpeg-location', path.ffmpeg_folder()]
def wahiddl_list():
    return['yt-dlp', '--batch-file', 'url_list.txt', '-c', '-S', 'quality,res,fps,hdr:12,channels,size,br,asr', '--throttled-rate', '100K', '--merge-output-format', 'mp4', '--ffmpeg-location', path.ffmpeg_folder()]
def wahiddl_audio():
    return['yt-dlp', '-c', '--throttled-rate', '100K', '--extract-audio', '-f', 'bestaudio[ext=m4a]', '--ffmpeg-location', path.ffmpeg_folder()]
def wahiddl_CS():
    return['yt-dlp', '--cookies-from-browser', 'chrome', '-c', '-S', 'quality,res,fps,hdr:12,channels,size,br,asr', '--throttled-rate', '100K', '--merge-output-format', 'mp4', '--ffmpeg-location', path.ffmpeg_folder()]