#Platform info
import sys
def vi_platform():
    if sys.platform  == "win32":
        system_os = "Windows"
        return system_os
    elif sys.platform  == "linux":
        system_os = "Linux"
        return system_os
    elif sys.platform == "darwin":
        system_os = "macOS"
        return system_os
#Wahid-dl info
channel = "Develop"
number = "6.0"
build_number = "20250428.1"
language = "Python"
def vi_detail():
    vi = [channel, number, build_number, language]
    return vi