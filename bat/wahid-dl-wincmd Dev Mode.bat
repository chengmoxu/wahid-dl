@echo off
echo wahid-dl Dev Mode
echo Version: 5.1
echo Build: wahid-dl.v5.1.20240906.windows-cmd.1
echo ------------------------------------------------------------
set /p var=yt-dlp命令模式，請直接輸入yt-dlp命令:
echo ------------------------------------------------------------
cd C:\wahid-dl
yt-dlp -U
yt-dlp %var%
pause