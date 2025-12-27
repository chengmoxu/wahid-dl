#Platform info
import sys
def vi_platform(): #current execution platform detection function
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
channel = "Stable"
number = "6.2"
build_number = "20251227.1"
language = "Python"
def vi_detail():
    vi = [channel, number, build_number, language] #vi = version info
    return vi