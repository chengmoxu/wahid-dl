import os
from packages.core import version_info
wahiddl_DEV_folder_name = "wahid-dl DEV"
def checking_wahiddl_DEV_folder_existed():
    if version_info.vi_platform() == "Windows":
        path = os.path.join("C:\\", "wahid-dl DEV")
    elif version_info.vi_platform() == "Linux":
        path = os.path.expanduser("~/wahid-dl DEV")
    else:
        return False, "Unsupported OS"
    try:
        wahiddl_DEV_folder_existed = os.path.exists(path)
        return wahiddl_DEV_folder_existed
    except Exception as error:
        return False, str(error)