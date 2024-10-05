@echo off
echo wahid-dl Cookies Support
echo ------------------------------------------------------------
set /p var=請輸入欲下載影片之網址:
echo ------------------------------------------------------------
echo 執行開始
echo ------------------------------------------------------------
cd C:\wahid-dl
yt-dlp -U
yt-dlp --cookies-from-browser chrome -c -S"quality,res,fps,hdr:12,channels,size,br,asr" --throttled-rate 100K --merge-output-format mp4 --ffmpeg-location "C:\FFmpeg" %var%
echo ------------------------------------------------------------
echo 執行結束，請至資料夾內確認您的下載
echo ------------------------------------------------------------
pause