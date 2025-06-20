from packages.core import version_info
from packages.function import wahiddl
system_os = version_info.vi_platform()
try: 
    wahiddl.main()
except:
    print ("不支援的平台")
input()