from packages.core import version_info
from packages.function import wahiddl_devmode
system_os = version_info.vi_platform()
if system_os  == "Windows":
    wahiddl_devmode.devmode()
elif system_os  == "Linux":
    wahiddl_devmode.devmode()
elif system_os == "macOS":
    print ("暫時不支援")
else:
    print ("不支援的平台")
input()