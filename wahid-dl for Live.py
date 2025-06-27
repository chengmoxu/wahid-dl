from packages.core import version_info
from packages.function import wahiddl_live
system_os = version_info.vi_platform()
try: 
    wahiddl_live.main()
except:
    print ("不支援的平台")
input()