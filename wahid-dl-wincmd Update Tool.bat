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
move C:\wahid-dl\updates\wahid-dl-main\*.* C:\wahid-dl\
del updates.zip
del C:\wahid-dl\updates\wahid-dl-main\*.*
echo ------------------------------------------------------------
echo ��s����
echo ------------------------------------------------------------
pause