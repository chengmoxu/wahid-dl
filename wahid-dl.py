#from packages.core import version_info
from packages.function import wahiddl
#system_os = version_info.vi_platform() # from import 'version_info' checking current platform and
try:
    wahiddl.main() # from packages.function import the 'wahiddl'and execute its function main()
except:
    print ("不支援的平台")
input()