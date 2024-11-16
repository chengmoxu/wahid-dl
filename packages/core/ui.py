from packages.core import system_os
from packages.core import version_info
system_os = system_os.get_system_os()
programming_language = version_info.get_version_programming_language()
title_wahiddl = "wahid-dl [" + system_os + "] [" + programming_language + "]"
title_wahiddl_tool = "wahid-dl Tool [" + system_os + "] [" + programming_language + "]"
title_wahiddl_devmode = "wahid-dl Dev Mode [" + system_os + "] [" + programming_language + "]" + "\n" + version_info.get_version_outline()
def get_title_wahiddl():
    return title_wahiddl
def get_title_wahiddl_tool():
    return title_wahiddl_tool
def get_title_wahiddl_devmode():
    return title_wahiddl_devmode
def get_ui_start():
    print ("------------------------------------------------------------")
    print ("任務開始執行")
    print ("------------------------------------------------------------")
def get_ui_exit():
    print ("------------------------------------------------------------")
    print ("即將結束程式，請按下任意鍵退出程式")
    print ("------------------------------------------------------------")