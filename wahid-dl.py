from packages.core import version_info
from packages.function import wahiddl
system_os = version_info.vi_platform()
if system_os  == "Windows":
    wahiddl.main()
elif system_os  == "Linux":
    print ("暫時不支援")
elif system_os == "macOS":
    print ("暫時不支援")
else:
    print ("不支援的平台")
input()