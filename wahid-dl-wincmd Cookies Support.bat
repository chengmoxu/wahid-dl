@echo off
echo wahid-dl Cookies Support
echo ------------------------------------------------------------
set /p var=�п�J���U���v�������}:
echo ------------------------------------------------------------
echo �U���}�l
echo ------------------------------------------------------------
cd C:\wahid-dl
yt-dlp -U
yt-dlp --cookies-from-browser chrome -c -S"quality,res,fps,hdr:12,channels,size,br,asr" --throttled-rate 100K --merge-output-format mp4 %var%
echo ------------------------------------------------------------
echo ���浲���A�Цܸ�Ƨ����T�{�z���U��
echo ------------------------------------------------------------
pause