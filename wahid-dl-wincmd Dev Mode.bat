@echo off
echo wahid-dl Dev Mode
echo Version: 3.4
echo Build: wahid-dl.v3.4.20240626.windows-cmd.1
echo ------------------------------------------------------------
set /p var=yt-dlp命令模式，請直接輸入yt-dlp命令:
echo ------------------------------------------------------------
cd C:\wahid-dl
yt-dlp -U
yt-dlp %var%
pause