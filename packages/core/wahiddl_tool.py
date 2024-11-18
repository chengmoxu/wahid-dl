import os
from packages.core import system_os
from packages.checker import checking_wahiddl
from packages.checker import checking_wahiddl_DEV
from packages.checker import checking_ytdlp
from packages.checker import checking_ffmpeg
from packages.installer import installer_wahiddl
from packages.installer import installer_wahiddl_DEV
from packages.installer import installer_ytdlp
from packages.installer import installer_ffmpeg
from packages.uninstaller import uninstaller_wahiddl
from packages.uninstaller import uninstaller_wahiddl_DEV
from packages.uninstaller import uninstaller_ytdlp
from packages.uninstaller import uninstaller_ffmpeg
from packages.core import version_info
from packages.core import ui
system_os = system_os.get_system_os()
def wahiddl_tool_windows():
    print(ui.ASCII_art())
    print ("wahid-dl Tool [" + system_os + "]")
    print (version_info.get_version_outline())
    mode = "start"
    while mode == "start":
        print ("1: 完整安裝/更新 wahid-dl 及附屬依賴工具")
        print ("2: 更新 wahid-dl 主程式")
        print ("3: 更新 yt-dlp")
        print ("4: 更新 FFmpeg")
        print ("DEVINSTALL: 安裝/更新 wahid-dl DEV 主程式")
        print ("0: 離開程式")
        userinput = input ("請選擇執行項目: ")
        userinput_judge = str.isdigit(userinput)
        if userinput_judge == True: 
            if userinput == "0":
                ui.ui_exit()
                break
            elif userinput == "1":
                print ("完整安裝/更新 wahid-dl 及附屬依賴工具")
                print ("安裝 wahid-dl 主程式")
                wahiddl_status = checking_wahiddl.checking_wahiddl_folder_existed()[0]
                if wahiddl_status == True:
                    uninstaller_wahiddl.uninstaller_wahiddl_uninstall()
                    installer_wahiddl.installer_wahiddl_install()
                elif wahiddl_status == False:
                    os.mkdir ('C:\\wahid-dl')
                    installer_wahiddl.installer_wahiddl_install()
                print ("安裝 yt-dlp")
                ytdlp_status = checking_ytdlp.checking_wahiddl_ytdlp_existed()[0]
                if ytdlp_status == True:
                    installer_ytdlp.installer_wahiddl_ytdlp_update()
                elif ytdlp_status == False:
                    installer_ytdlp.installer_wahiddl_ytdlp_install()
                print ("安裝 FFmpeg")
                uninstaller_ffmpeg.uninstaller_old_ffmpeg()
                ffmpeg_folder_status = checking_ffmpeg.checking_ffmpeg_folder_existed()[0]
                if ffmpeg_folder_status == True:
                    ffmpeg_exe_status = checking_ffmpeg.checking_ffmpeg_files_existed()[0]
                    ffplay_exe_status = checking_ffmpeg.checking_ffmpeg_files_existed()[1]
                    ffprobe_exe_status = checking_ffmpeg.checking_ffmpeg_files_existed()[2]
                    if ffmpeg_exe_status == True and ffplay_exe_status == True and ffprobe_exe_status == True:
                        ffmpeg_version_status = checking_ffmpeg.checking_ffmpeg_version()
                        if ffmpeg_version_status == 'unnecessary':
                            continue
                        elif ffmpeg_version_status == 'need':
                            uninstaller_ffmpeg.uninstaller_ffmpeg()
                            installer_ffmpeg.installer_ffmpeg()
                elif ffmpeg_folder_status == False:
                    os.mkdir ('C:\\FFmpeg')
                    installer_ffmpeg.installer_ffmpeg()
                ui.ui_exit()
                break
            elif userinput == "2":
                print ("安裝 wahid-dl 主程式")
                wahiddl_status = checking_wahiddl.checking_wahiddl_folder_existed()[0]
                if wahiddl_status == True:
                    uninstaller_wahiddl.uninstaller_wahiddl_uninstall()
                    installer_wahiddl.installer_wahiddl_install()
                elif wahiddl_status == False:
                    os.mkdir ('C:\\wahid-dl')
                    installer_wahiddl.installer_wahiddl_install()
                ui.ui_exit()
                break
            elif userinput == "3":
                print ("安裝 yt-dlp")
                if checking_ytdlp.checking_wahiddl_ytdlp_existed() == True:
                    installer_ytdlp.installer_wahiddl_ytdlp_update()
                elif checking_ytdlp.checking_wahiddl_ytdlp_existed() == False:
                    installer_ytdlp.installer_wahiddl_ytdlp_install()
                ui.ui_complete()
                ui.ui_exit()
                break
            elif userinput == "4":
                print ("安裝 FFmpeg")
                uninstaller_ffmpeg.uninstaller_old_ffmpeg()
                ffmpeg_folder_status = checking_ffmpeg.checking_ffmpeg_folder_existed()[0]
                if ffmpeg_folder_status == True:
                    ffmpeg_exe_status = checking_ffmpeg.checking_ffmpeg_files_existed()[0]
                    ffplay_exe_status = checking_ffmpeg.checking_ffmpeg_files_existed()[1]
                    ffprobe_exe_status = checking_ffmpeg.checking_ffmpeg_files_existed()[2]
                    if ffmpeg_exe_status == True and ffplay_exe_status == True and ffprobe_exe_status == True:
                        ffmpeg_version_status = checking_ffmpeg.checking_ffmpeg_version()
                        if ffmpeg_version_status == 'unnecessary':
                            continue
                        elif ffmpeg_version_status == 'need':
                            uninstaller_ffmpeg.uninstaller_ffmpeg()
                            installer_ffmpeg.installer_ffmpeg()
                elif ffmpeg_folder_status == False:
                    os.mkdir ('C:\\FFmpeg')
                    installer_ffmpeg.installer_ffmpeg()
                ui.ui_exit()
                break
            else:
                print ("請重新輸入正確選項！")
        elif userinput_judge == False:
            if userinput == "DEVINSTALL":
                ui.ui_start()
                print ("安裝 wahid-dl DEV 主程式")
                if checking_wahiddl_DEV.checking_wahiddl_DEV_folder_existed() == True:
                    uninstaller_wahiddl_DEV.uninstaller_wahiddl_DEV_uninstall()
                    installer_wahiddl_DEV.installer_wahiddl_DEV_install()
                elif checking_wahiddl_DEV.checking_wahiddl_DEV_folder_existed()[0] == False:
                    if checking_wahiddl_DEV.checking_wahiddl_DEV_folder_existed()[1] == "Unsupported OS":
                        print (checking_wahiddl_DEV.checking_wahiddl_DEV_folder_existed()[1])
                        continue
                    else:
                        print (checking_wahiddl_DEV.checking_wahiddl_DEV_folder_existed()[1])
                        os.mkdir ('C:\\wahid-dl DEV')
                        installer_wahiddl_DEV.installer_wahiddl_DEV_install()
                print ("------------------------------------------------------------")
                print ("安裝 yt-dlp")
                if checking_ytdlp.checking_wahiddl_DEV_ytdlp_existed() == True:
                    installer_ytdlp.installer_wahiddl_DEV_ytdlp_update()
                elif checking_ytdlp.checking_wahiddl_DEV_ytdlp_existed() == False:
                    installer_ytdlp.installer_wahiddl_DEV_ytdlp_install()
                ui.ui_complete()
                ui.ui_exit()
                break
            else:
                print ("請重新輸入正確選項！")