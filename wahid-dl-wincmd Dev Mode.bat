@echo off
echo wahid-dl Dev Mode
echo Version: 3.2
echo Build: wahid-dl.v3.2.20240614.windows-cmd.2
echo ------------------------------------------------------------
set /p var=yt-dlp命令模式，請直接輸入yt-dlp命令:
echo ------------------------------------------------------------
cd C:\wahid-dl
yt-dlp -U
yt-dlp %var%
pause