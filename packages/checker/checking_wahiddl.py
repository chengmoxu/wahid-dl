import os
from packages.core import info
wahiddl_folder_name = "wahid-dl"
def folder():
    if info.platform() == "Windows":
        path = os.path.join("C:\\", "wahid-dl")
    elif info.platform() == "Linux":
        path = os.path.expanduser("~/wahid-dl")
    else:
        return False
    try:
        wahiddl_folder_existed = os.path.exists(path)
        return wahiddl_folder_existed
    except:
        return False