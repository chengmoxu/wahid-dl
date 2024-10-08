from packages.checking import checking_system_os
from packages.core import version_info
system_os = checking_system_os.get_system_os()
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