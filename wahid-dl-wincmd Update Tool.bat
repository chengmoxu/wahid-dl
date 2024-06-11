@echo off
echo wahid-dl 更新工具
echo ------------------------------------------------------------
echo 開始執行
echo ------------------------------------------------------------
echo 更新 yt-dlp
cd C:\wahid-dl
yt-dlp -U
echo ------------------------------------------------------------
echo 更新 ffmpeg
cd C:\wahid-dl
curl -o ffmpeg.zip https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip
mkdir ffmpeg
tar -zxvf ffmpeg.zip -C C:\wahid-dl\ffmpeg
move C:\wahid-dl\ffmpeg\*.exe C:\wahid-dl\
del ffmpeg.zip
rd /s/q C:\wahid-dl\ffmpeg
echo ------------------------------------------------------------
echo 更新 wahid-dl
cd C:\wahid-dl
curl -o updates.zip https://codeload.github.com/chengmoxu/wahid-dl/zip/refs/heads/main
mkdir updates
tar -zxvf updates.zip -C C:\wahid-dl\updates
move C:\wahid-dl\updates\wahid-dl-main\*.bat C:\wahid-dl\
del updates.zip
rd /s/q C:\wahid-dl\updates
echo ------------------------------------------------------------
echo 執行完成
echo ------------------------------------------------------------
pause