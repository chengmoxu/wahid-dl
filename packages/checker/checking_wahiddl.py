import os
from packages.core import version_info
wahiddl_folder_name = "wahid-dl"
def checking_wahiddl_folder_existed():
    if version_info.vi_platform() == "Windows":
        path = os.path.join("C:\\", "wahid-dl")
    elif version_info.vi_platform() == "Linux":
        path = os.path.expanduser("~/wahid-dl")
    else:
        return False
    try:
        wahiddl_folder_existed = os.path.exists(path)
        return wahiddl_folder_existed
    except:
        return False