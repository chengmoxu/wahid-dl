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
move "C:\wahid-dl\updates\wahid-dl-main\*.py" "C:\wahid-dl\"
del "C:\wahid-dl\updates.zip"
rd /s /q "C:\wahid-dl\updates"
echo ------------------------------------------------------------
echo 更新 yt-dlp
cd "C:\wahid-dl"
yt-dlp -U
echo ------------------------------------------------------------
echo 下載 FFmpeg
cd "C:\wahid-dl"
del ffmpeg.exe ffplay.exe ffprobe.exe
mkdir "C:\FFmpeg"
cd "C:\FFmpeg"
del ffmpeg.exe ffplay.exe ffprobe.exe
curl -L -o ffmpeg.zip https://github.com/GyanD/codexffmpeg/releases/download/7.0.2/ffmpeg-7.0.2-full_build.zip
mkdir "C:\FFmpeg\FFmpeg-unzip"
tar -zxvf ffmpeg.zip -C "C:\FFmpeg\FFmpeg-unzip"
move "C:\FFmpeg\FFmpeg-unzip\ffmpeg-7.0.2-full_build\bin\*.exe" "C:\FFmpeg\"
setx PATH "FFmpeg;C:\FFmpeg\"
del "C:\FFmpeg\ffmpeg.zip"
rd /s /q "C:\FFmpeg\ffmpeg-unzip"
echo ------------------------------------------------------------
echo 執行完成，請至資料夾內確認更新
echo ------------------------------------------------------------
pause