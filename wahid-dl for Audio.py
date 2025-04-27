from packages.core import version_info
from packages.function import wahiddl_audio
system_os = version_info.vi_platform()
if system_os  == "Windows":
    wahiddl_audio.main()
elif system_os  == "Linux":
    print ("暫時不支援")
elif system_os == "macOS":
    print ("暫時不支援")
else:
    print ("不支援的平台")
input()