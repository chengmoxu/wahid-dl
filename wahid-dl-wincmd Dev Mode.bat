@echo off
echo wahid-dl Dev Mode
echo Version: 2.1
echo Build: wahid-dl.v2.1.20231113.windows-cmd.1
echo ------------------------------------------------------------
set /p var=yt-dlp命令模式，請直接輸入yt-dlp命令:
echo ------------------------------------------------------------
cd C:\wahid-dl
yt-dlp %var%
pause