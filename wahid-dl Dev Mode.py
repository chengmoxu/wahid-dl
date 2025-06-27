from packages.core import version_info
from packages.function import wahiddl_devmode
system_os = version_info.vi_platform()
try:
    wahiddl_devmode.devmode()
except:
    print ("不支援的平台")
input()