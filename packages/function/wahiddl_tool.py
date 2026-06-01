import os
from packages.checker import checking_wahiddl
from packages.checker import checking_wahiddl_beta
from packages.checker import checking_ytdlp
from packages.checker import checking_ffmpeg
from packages.installer import installer_wahiddl
from packages.installer import installer_wahiddl_beta
from packages.installer import installer_ytdlp
from packages.installer import installer_ffmpeg
from packages.uninstaller import uninstaller_wahiddl
from packages.uninstaller import uninstaller_wahiddl_beta
from packages.uninstaller import uninstaller_ytdlp
from packages.uninstaller import uninstaller_ffmpeg
from packages.core import ui
def main():
    print(ui.ASCII_art())
    print(ui.detail_wahiddl_tool())
    mode = ""
    while mode == "":
        print(ui.divider())
        print("1: 完整安裝/更新 wahid-dl 及附屬依賴工具")
        print("2: 安裝/更新 wahid-dl 主程式")
        print("3: 安裝/更新 yt-dlp")
        print("4: 安裝 FFmpeg")
        print("5: 完整解除安裝 wahid-dl 及附屬依賴工具")
        print("6: 解除安裝 wahid-dl 主程式")
        print("7: 解除安裝 yt-dlp")
        print("8: 解除安裝 FFmpeg")
        print("BETAINSTALL: 安裝/更新 wahid-dl (Beta)")
        print("BETAUNINSTALL: 解除安裝 wahid-dl (Beta)")
        print("0: 離開程式")
        print(ui.divider())
        userinput = input ("請選擇執行項目: ")
        userinput_judge = str.isdigit(userinput)
        if userinput_judge == True: 
            if userinput == "0":
                mode = "0"
            elif userinput == "1":
                print(ui.start())
                print("完整安裝/更新 wahid-dl 及附屬依賴工具")
                print(ui.divider())
                print("安裝 wahid-dl 主程式")
                wahiddl_status = checking_wahiddl.folder()
                if wahiddl_status == True:
                    uninstaller_wahiddl.uninstall()
                    installer_wahiddl.install()
                elif wahiddl_status == False:
                    os.mkdir ('C:\\wahid-dl')
                    installer_wahiddl.install()
                print(ui.divider())
                print("安裝/更新 yt-dlp")
                ytdlp_status = checking_ytdlp.ytdlp()
                if ytdlp_status == True:
                    installer_ytdlp.update()
                elif ytdlp_status == False:
                    installer_ytdlp.install()
                print(ui.divider())
                print("安裝 FFmpeg")
                uninstaller_ffmpeg.v1()
                ffmpeg_folder_status = checking_ffmpeg.folder()
                if ffmpeg_folder_status == True:
                    if checking_ffmpeg.files()[0] == True and checking_ffmpeg.files()[1] == True and checking_ffmpeg.files()[2] == True:
                        if checking_ffmpeg.version() == False:
                            continue
                        else:
                            uninstaller_ffmpeg.v2()
                            installer_ffmpeg.v2()
                    else:
                        installer_ffmpeg.v2()
                elif ffmpeg_folder_status == False:
                    os.mkdir ('C:\\FFmpeg')
                    installer_ffmpeg.v2()
                print(ui.complete())
                mode = ""
            elif userinput == "2":
                print(ui.start())
                print("安裝/更新 wahid-dl 主程式")
                if checking_wahiddl.folder() == True:
                    uninstaller_wahiddl.uninstall()
                    installer_wahiddl.install()
                elif checking_wahiddl.folder() == False:
                    try:
                        os.mkdir ('C:\\wahid-dl')
                        installer_wahiddl.install()
                    except:
                        print("不支援的平台")
                print(ui.complete())
                mode = ""
            elif userinput == "3":
                print(ui.start())
                print("安裝/更新 yt-dlp")
                if checking_ytdlp.ytdlp() == True:
                    installer_ytdlp.update()
                elif checking_ytdlp.ytdlp() == False:
                    installer_ytdlp.install()
                print(ui.complete())
                mode = ""
            elif userinput == "4":
                print(ui.start())
                print("安裝 FFmpeg")
                uninstaller_ffmpeg.v1()
                ffmpeg_folder_status = checking_ffmpeg.folder()
                if ffmpeg_folder_status == True:
                    if checking_ffmpeg.files()[0] == True and checking_ffmpeg.files()[1] == True and checking_ffmpeg.files()[2] == True:
                        if checking_ffmpeg.version() == False:
                            continue
                        else:
                            try:
                                uninstaller_ffmpeg.v2()
                                installer_ffmpeg.v2()
                            except:
                                uninstaller_ffmpeg.v2()
                                installer_ffmpeg.v2()
                    else:
                        try:
                            installer_ffmpeg.v2()
                        except:
                                installer_ffmpeg.v2()
                elif ffmpeg_folder_status == False:
                    os.mkdir ('C:\\FFmpeg')
                    installer_ffmpeg.v2()
                print(ui.complete())
                mode = ""
            elif userinput == "5":
                print(ui.start())
                print("完整解除安裝 wahid-dl 及附屬依賴工具")
                print(ui.divider())
                print("解除安裝 wahid-dl 主程式")
                wahiddl_status = checking_wahiddl.folder()
                if wahiddl_status == True:
                    uninstaller_wahiddl.uninstall()
                elif wahiddl_status == False:
                    print("wahid-dl 主程式已不存在")
                print(ui.divider())
                print("解除安裝 yt-dlp")
                ytdlp_status = checking_ytdlp.ytdlp()
                if ytdlp_status == True:
                    uninstaller_ytdlp.uninstall()
                elif ytdlp_status == False:
                    print("yt-dlp 已不存在")
                print(ui.divider())
                print("解除安裝 FFmpeg")
                uninstaller_ffmpeg.v1()
                if checking_ffmpeg.folder() == True:
                    if checking_ffmpeg.files()[0] == True and checking_ffmpeg.files()[1] == True and checking_ffmpeg.files()[2] == True:
                        uninstaller_ffmpeg.v2()
                    else:
                        print("FFmpeg 已不存在")
                else:
                    print("FFmpeg 已不存在")
                print(ui.complete())
                mode = ""
            elif userinput == "6":
                print(ui.start())
                print("解除安裝 wahid-dl 主程式")
                wahiddl_status = checking_wahiddl.folder()
                if wahiddl_status == True:
                    uninstaller_wahiddl.uninstall()
                elif wahiddl_status == False:
                    print("wahid-dl 主程式已不存在")
                print(ui.complete())
                mode = ""
            elif userinput == "7":
                print(ui.start())
                print("解除安裝 yt-dlp")
                ytdlp_status = checking_ytdlp.ytdlp()
                if ytdlp_status == True:
                    uninstaller_ytdlp.uninstall()
                elif ytdlp_status == False:
                    print("yt-dlp 已不存在")
                print(ui.complete())
                mode = ""
            elif userinput == "8":
                print(ui.start())
                print("解除安裝 FFmpeg")
                uninstaller_ffmpeg.v1()
                if checking_ffmpeg.folder() == True:
                    if checking_ffmpeg.files()[0] == True and checking_ffmpeg.files()[1] == True and checking_ffmpeg.files()[2] == True:
                        uninstaller_ffmpeg.v2()
                    else:
                        print("FFmpeg 已不存在")
                else:
                    print("FFmpeg 已不存在")
                print(ui.complete())
                mode = ""
            else:
                print("請重新輸入正確選項！")
                mode = ""
        elif not userinput_judge:
            if userinput == "BETAINSTALL":
                print(ui.start())
                print("安裝/更新 wahid-dl (Beta)")
                if checking_wahiddl_beta.folder() == True:
                    uninstaller_wahiddl_beta.uninstall()
                    installer_wahiddl_beta.install()
                elif checking_wahiddl_beta.folder() == False:
                    try:
                        os.mkdir ('C:\\wahid-dl (Beta)')
                        installer_wahiddl_beta.install()
                    except:
                        print("不支援的平台")
                print(ui.divider())
                print("安裝/更新 yt-dlp in wahid-dl (Beta)")
                if checking_ytdlp.beta_ytdlp() == True:
                    installer_ytdlp.beta_update()
                elif checking_ytdlp.beta_ytdlp() == False:
                    installer_ytdlp.beta_install()
                print(ui.complete())
                mode = ""
            elif userinput == "BETAUNINSTALL":
                print(ui.start())
                print("解除安裝 wahid-dl (Beta)")
                if checking_wahiddl_beta.folder() == True:
                    uninstaller_wahiddl_beta.uninstall()
                elif checking_wahiddl_beta.folder() == False:
                    print("wahid-dl (Beta) 已不存在")
                print(ui.divider())
                print("解除安裝 yt-dlp in wahid-dl (Beta)")
                if checking_ytdlp.beta_ytdlp() == True:
                    uninstaller_ytdlp.beta_uninstall()
                elif checking_ytdlp.beta_ytdlp() == False:
                    print("yt-dlp in wahid-dl (Beta) 已不存在")
                print(ui.complete())
                mode = ""
            else:
                print("請重新輸入正確選項！")
                mode = ""
    while mode == "0":
        ui.exit()
        break