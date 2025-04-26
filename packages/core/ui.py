from packages.core import version_info
#ASCII art
def ASCII_art():
    return("      ###       ###        ###         ###     ###         #######      ########             #########       ###\n"
           "     ###       ###      ###   ##      ###     ###         ###          ###    ###           ###    ###      ###\n"
           "    ###       ###     ###    ##      ###     ###         ###          ###    ###           ###    ###      ###\n"
           "   >>>  >>>  >>>    >>>>>>>>>>>     >>>>>>>>>>>         >>>          >>>    >>>   >>>>>   >>>    >>>      >>>\n"
           "  ### ##  # ###    ###      ##     ###     ###         ###          ###    ###           ###    ###      ###\n"
           " #####    ###     ###      ##     ###     ###         ###          ###    ###           ###    ###      ###\n"
           "####      ##     ###      ##     ###     ###     #######          #########            #########       ###")
#Title with version info
vi=str(" [" + str(version_info.vi_platform()) + "] [" + str(version_info.vi_detail()[0]) + "]v" + str(version_info.vi_detail()[1] + version_info.vi_detail()[2]) + "-" + str(version_info.vi_detail()[3]))
def ui_title_wahiddl():
    title_wahiddl = "wahid-dl" + vi
    return title_wahiddl
def ui_title_wahiddl_tool():
    title_wahiddl_tool = "wahid-dl Tool" + vi
    return title_wahiddl_tool
def ui_title_wahiddl_devmode():
    title_wahiddl_devmode = "wahid-dl Dev Mode" + vi
    return title_wahiddl_devmode
def ui_title_wahiddl_format_checking_tool():
    title_wahiddl_format_checking_tool = "wahid-dl Format Checking Tool" + vi
    return title_wahiddl_format_checking_tool
def ui_title_wahiddl_S():
    title_wahiddl_S = "wahid-dl for wahid-dl for Subtitle" + vi
    return title_wahiddl_S
def ui_title_wahiddl_QS():
    title_wahiddl_QS = "wahid-dl for Quality Selection" + vi
    return title_wahiddl_QS
def ui_title_wahiddl_live():
    title_wahiddl_live = "wahid-dl for Live" + vi
    return title_wahiddl_live
def ui_title_wahiddl_list():
    title_wahiddl_list = "wahid-dl for List" + vi
    return title_wahiddl_list
def ui_title_wahiddl_audio():
    title_wahiddl_audio = "wahid-dl for Audio" + vi
    return title_wahiddl_audio
def ui_title_wahiddl_CS():
    title_wahiddl_CS = "wahid-dl for Cookies Support" + vi
    return title_wahiddl_CS
#Unified UI for task execution status
def ui_start():
    print ("------------------------------------------------------------")
    print ("任務開始執行")
    print ("------------------------------------------------------------")
def ui_exit():
    print ("------------------------------------------------------------")
    print ("即將結束程式，請按下Enter鍵退出程式")
    print ("------------------------------------------------------------")
def ui_complete():
    print ("------------------------------------------------------------")
    print ("任務執行結束")
    print ("------------------------------------------------------------")