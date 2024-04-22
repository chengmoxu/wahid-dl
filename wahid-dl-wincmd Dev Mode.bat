@echo off
echo wahid-dl Dev Mode
echo Version: 2.2
echo Build: wahid-dl.v2.2.20240422.windows-cmd.1
echo ------------------------------------------------------------
set /p var=yt-dlp命令模式，請直接輸入yt-dlp命令:
echo ------------------------------------------------------------
cd C:\wahid-dl
yt-dlp -U
yt-dlp %var%
pause