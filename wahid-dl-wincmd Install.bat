@echo off
echo wahid-dl �w�ˤu��
echo ------------------------------------------------------------
echo �}�l����
echo ------------------------------------------------------------
echo �إ߸�Ƨ�
cd "C:\"
mkdir wahid-dl
echo ------------------------------------------------------------
echo �U�� yt-dlp
cd "C:\wahid-dl"
curl https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe
echo ------------------------------------------------------------
echo �U�� ffmpeg
cd "C:\wahid-dl"
curl -o ffmpeg.zip https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip
mkdir ffmpeg
tar -zxvf ffmpeg.zip -C "C:\wahid-dl\ffmpeg"
move "C:\wahid-dl\ffmpeg\ffmpeg-master-latest-win64-gpl\bin\*.exe" "C:\wahid-dl\" -Force
del ffmpeg.zip
rd /s/q C:\wahid-dl\ffmpeg
echo ------------------------------------------------------------
echo �w�� wahid-dl
cd "C:\wahid-dl"
curl -o updates.zip https://codeload.github.com/chengmoxu/wahid-dl/zip/refs/heads/main
mkdir updates
tar -zxvf updates.zip -C "C:\wahid-dl\updates"
move "C:\wahid-dl\updates\wahid-dl-main\*.bat" "C:\wahid-dl\"
del updates.zip
rd /s/q C:\wahid-dl\updates
echo ------------------------------------------------------------
echo ���槹��
echo ------------------------------------------------------------
pause