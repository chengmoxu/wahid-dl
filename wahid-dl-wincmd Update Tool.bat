@echo off
echo wahid-dl ��s�u��
echo ------------------------------------------------------------
echo �}�l��s
echo ------------------------------------------------------------
cd C:\wahid-dl
yt-dlp -U
curl -o updates.zip https://codeload.github.com/chengmoxu/wahid-dl/zip/refs/heads/main
mkdir updates
tar -zxvf updates.zip -C C:\wahid-dl\updates
move C:\wahid-dl\updates\wahid-dl-main\*.bat C:\wahid-dl\
del updates.zip
rd /Y C:\wahid-dl\updates
echo ------------------------------------------------------------
echo ��s����
echo ------------------------------------------------------------
pause