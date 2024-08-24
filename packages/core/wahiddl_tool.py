from packages.checking import checking_system_os
from packages.checking import checking_wahiddl
from packages.checking import checking_wahiddl_DEV
from packages.checking import checking_ytdlp
from packages.checking import checking_ffmpeg
from packages.installer import installer_wahiddl
from packages.installer import installer_wahiddl_DEV
from packages.installer import installer_ytdlp
from packages.installer import installer_ffmpeg
from packages.uninstaller import uninstaller_wahiddl
from packages.uninstaller import uninstaller_wahiddl_DEV
from packages.uninstaller import uninstaller_ytdlp
from packages.uninstaller import uninstaller_ffmpeg
from packages.core import version_info
system_os = checking_system_os.get_system_os()
def wahiddl_tool_windows():
    def exit():
        print ("------------------------------------------------------------")
        print ("即將結束程式")
        print ("------------------------------------------------------------")
    print ("wahid-dl Tool [" + system_os + "]")
    display_version_outline = version_info.get_version_outline()
    print (display_version_outline)
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
                exit()
                break
            elif userinput == "1":
                print ("完整安裝/更新 wahid-dl 及附屬依賴工具")
                print ("安裝 wahid-dl 主程式")
                error_status = ''
                wahiddl_status = checking_wahiddl.checking_wahiddl_folder_existed()[0]
                error_status = checking_wahiddl.checking_wahiddl_folder_existed()[1]
                if wahiddl_status == 'True':
                    uninstaller_wahiddl.uninstaller_wahiddl_uninstall()
                    installer_wahiddl.installer_wahiddl_install()
                elif wahiddl_status == 'Flase':
                    installer_wahiddl.installer_wahiddl_install()
                elif error_status != 'False':
                    print (wahiddl_status)
                    print (error_status)
                print ("安裝 yt-dlp")
                error_status = ''
                ytdlp_status = checking_ytdlp.checking_wahiddl_ytdlp_file_existed()[0]
                error_status = checking_ytdlp.checking_wahiddl_ytdlp_file_existed()[1]
                if ytdlp_status == 'True' and error_status == 'False':
                    uninstaller_ytdlp.uninstaller_wahiddl_ytdlp_uninstall()
                    installer_ytdlp.installer_wahiddl_ytdlp_install()
                elif ytdlp_status == 'Flase' and error_status == 'False':
                    installer_ytdlp.installer_wahiddl_ytdlp_update()
                elif error_status != 'False':
                    print (ytdlp_status)
                    print (error_status)
                print ("安裝 FFmpeg")
                uninstaller_ffmpeg.uninstaller_old_ffmpeg()
                error_status = ''
                ffmpeg_folder_status = checking_ffmpeg.checking_ffmpeg_folder_existed()[0]
                if ffmpeg_folder_status == 'True':
                    error_status = ''
                    ffmpeg_exe_status = checking_ffmpeg.checking_ffmpeg_files_existed()[0]
                    ffplay_exe_status = checking_ffmpeg.checking_ffmpeg_files_existed()[1]
                    ffprobe_exe_status = checking_ffmpeg.checking_ffmpeg_files_existed()[2]
                    error_status = checking_ffmpeg.checking_ffmpeg_files_existed()[3]
                    if ffmpeg_exe_status == 'True' and ffplay_exe_status == 'True' and ffprobe_exe_status == 'True':
                        ffmpeg_version_status = checking_ffmpeg.checking_ffmpeg_version()
                        if ffmpeg_version_status == 'unnecessary':
                            continue
                        elif ffmpeg_version_status == 'need':
                            uninstaller_ffmpeg.uninstaller_ffmpeg()
                            installer_ffmpeg.installer_ffmpeg()
                    elif error_status != 'Flase':
                        print (ffmpeg_exe_status)
                        print (ffplay_exe_status)
                        print (ffprobe_exe_status)
                        print (error_status)
                elif ffmpeg_folder_status == 'Flase':
                    installer_ffmpeg.installer_ffmpeg()
                exit()
                break
            elif userinput == "2":
                print ("安裝 wahid-dl 主程式")
                error_status = ''
                wahiddl_status = checking_wahiddl.checking_wahiddl_folder_existed()[0]
                error_status = checking_wahiddl.checking_wahiddl_folder_existed()[1]
                if wahiddl_status == 'True':
                    uninstaller_wahiddl.uninstaller_wahiddl_uninstall()
                    installer_wahiddl.installer_wahiddl_install()
                elif wahiddl_status == 'Flase':
                    installer_wahiddl.installer_wahiddl_install()
                elif error_status != 'False':
                    print (wahiddl_status)
                    print (error_status)
                exit()
                break
            elif userinput == "3":
                print ("安裝 yt-dlp")
                error_status = ''
                ytdlp_status = checking_ytdlp.checking_wahiddl_ytdlp_file_existed()[0]
                error_status = checking_ytdlp.checking_wahiddl_ytdlp_file_existed()[1]
                if ytdlp_status == 'True' and error_status == 'False':
                    uninstaller_ytdlp.uninstaller_wahiddl_ytdlp_uninstall()
                    installer_ytdlp.installer_wahiddl_ytdlp_install()
                elif ytdlp_status == 'Flase' and error_status == 'False':
                    installer_ytdlp.installer_wahiddl_ytdlp_update()
                elif error_status != 'False':
                    print (ytdlp_status)
                    print (error_status)
                exit()
                break
            elif userinput == "4":
                print ("安裝 FFmpeg")
                uninstaller_ffmpeg.uninstaller_old_ffmpeg()
                error_status = ''
                ffmpeg_folder_status = checking_ffmpeg.checking_ffmpeg_folder_existed()[0]
                if ffmpeg_folder_status == 'True':
                    error_status = ''
                    ffmpeg_exe_status = checking_ffmpeg.checking_ffmpeg_files_existed()[0]
                    ffplay_exe_status = checking_ffmpeg.checking_ffmpeg_files_existed()[1]
                    ffprobe_exe_status = checking_ffmpeg.checking_ffmpeg_files_existed()[2]
                    error_status = checking_ffmpeg.checking_ffmpeg_files_existed()[3]
                    if ffmpeg_exe_status == 'True' and ffplay_exe_status == 'True' and ffprobe_exe_status == 'True':
                        ffmpeg_version_status = checking_ffmpeg.checking_ffmpeg_version()
                        if ffmpeg_version_status == 'unnecessary':
                            continue
                        elif ffmpeg_version_status == 'need':
                            uninstaller_ffmpeg.uninstaller_ffmpeg()
                            installer_ffmpeg.installer_ffmpeg()
                    elif error_status != 'Flase':
                        print (ffmpeg_exe_status)
                        print (ffplay_exe_status)
                        print (ffprobe_exe_status)
                        print (error_status)
                elif ffmpeg_folder_status == 'Flase':
                    installer_ffmpeg.installer_ffmpeg()
                exit()
                break
            else:
                print ("請重新輸入正確選項！")
        elif userinput_judge == False:
            if userinput == "DEVINSTALL":
                print ("安裝 wahid-dl DEV 主程式")
                error_status = ''
                wahiddl_DEV_status = checking_wahiddl_DEV.checking_wahiddl_DEV_folder_existed()[0]
                error_status = checking_wahiddl_DEV.checking_wahiddl_DEV_folder_existed()[1]
                if wahiddl_DEV_status == 'True':
                    uninstaller_wahiddl_DEV.uninstaller_wahiddl_DEV_uninstall()
                    installer_wahiddl_DEV.installer_wahiddl_DEV_install()
                elif wahiddl_DEV_status == 'Flase':
                    installer_wahiddl_DEV.installer_wahiddl_DEV_install()
                elif error_status != 'False':
                    print (wahiddl_DEV_status)
                    print (error_status)
                exit()
                break
            else:
                print ("請重新輸入正確選項！")