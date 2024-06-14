@echo off
echo wahid-dl 更新工具
echo ------------------------------------------------------------
echo 開始執行
echo ------------------------------------------------------------
echo 更新 wahid-dl
cd "C:\wahid-dl"
curl -L -o updates.zip https://codeload.github.com/chengmoxu/wahid-dl/zip/refs/heads/main
mkdir "C:\wahid-dl\updates"
tar -zxvf updates.zip -C "C:\wahid-dl\updates"
move "C:\wahid-dl\updates\wahid-dl-main\*.bat" "C:\wahid-dl\"
del "C:\wahid-dl\updates.zip"
rd /s /q "C:\wahid-dl\updates"
echo ------------------------------------------------------------
echo 更新 yt-dlp
cd "C:\wahid-dl"
yt-dlp -U
echo ------------------------------------------------------------
echo 更新 ffmpeg
cd "C:\wahid-dl"
curl -L -o ffmpeg.zip https://github.com/GyanD/codexffmpeg/releases/download/7.0.1/ffmpeg-7.0.1-full_build.zip
mkdir "C:\wahid-dl\ffmpeg"
tar -zxvf ffmpeg.zip -C "C:\wahid-dl\ffmpeg"
move "C:\wahid-dl\ffmpeg\ffmpeg-7.0.1-full_build\bin\*.exe" "C:\wahid-dl\"
del "C:\wahid-dl\ffmpeg.zip"
rd /s /q "C:\wahid-dl\ffmpeg"
echo ------------------------------------------------------------
echo 執行完成
echo ------------------------------------------------------------
pause