from packages.core import version_info
from packages.function import wahiddl_list
system_os = version_info.vi_platform()
try:
    wahiddl_list.main()
except:
    print ("不支援的平台")
input()