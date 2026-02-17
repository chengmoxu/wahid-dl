from packages.core import info
#ASCII art
def ASCII_art():
    return("      ###       ###        ###         ###     ###         ########     ########             #########       ###\n"
           "     ###       ###      ###   ##      ###     ###         ###          ###    ###           ###    ###      ###\n"
           "    ###       ###     ###    ##      ###     ###         ###          ###    ###           ###    ###      ###\n"
           "   >>>  >>>  >>>    >>>>>>>>>>>     >>>>>>>>>>>         >>>          >>>    >>>   >>>>>   >>>    >>>      >>>\n"
           "  ### ##  # ###    ###      ##     ###     ###         ###          ###    ###           ###    ###      ###\n"
           " #####    ###     ###      ##     ###     ###         ###          ###    ###           ###    ###      ###\n"
           "####      ##     ###      ##     ###     ###     #######          #########            #########       ###")

#title
def title_wahiddl():
    return "wahid-dl"
def title_wahiddl_beta():
    return "wahid-dl (Beta)"
def title_wahiddl_tool():
    return "wahid-dl Tool"
def title_wahiddl_devmode():
    return "wahid-dl Dev Mode"
def title_wahiddl_FCT():
    return "wahid-dl Format Checking Tool"
def title_wahiddl_subtitle():
    return "wahid-dl for wahid-dl for Subtitle"
def title_wahiddl_QS():
    return "wahid-dl for Quality Selection"
def title_wahiddl_live():
    return "wahid-dl for Live"
def title_wahiddl_list():
    return "wahid-dl for List"
def title_wahiddl_audio():
    return "wahid-dl for Audio"
def title_wahiddl_CS():
    return "wahid-dl for Cookies Support"

#detail = title with version info
vi=" [" + info.platform() + "] (" + info.version_detail()[0] + ") " + info.version_detail()[1] + "." + info.version_detail()[2] + "-" + info.version_detail()[3]
def detail_wahiddl():
    return "wahid-dl" + vi
def detail_wahiddl_tool():
    return "wahid-dl Tool" + vi
def detail_wahiddl_devmode():
    return "wahid-dl Dev Mode" + vi
def detail_wahiddl_FCT():
    return "wahid-dl Format Checking Tool" + vi
def detail_wahiddl_subtitle():
    return "wahid-dl for wahid-dl for Subtitle" + vi
def detail_wahiddl_QS():
    return "wahid-dl for Quality Selection" + vi
def detail_wahiddl_live():
    return "wahid-dl for Live" + vi
def detail_wahiddl_list():
    return "wahid-dl for List" + vi
def detail_wahiddl_audio():
    return "wahid-dl for Audio" + vi
def detail_wahiddl_CS():
    return "wahid-dl for Cookies Support" + vi

#unified UI for task execution status
def divider():
    return('==================================================')
def start():
    return('=================== 開 始 執 行 ===================')
def exit():
    return('========= 請 按 下 輸 入 鍵 以 離 開 程 式 =========')
def complete():
    return('=================== 執 行 結 束 ===================')