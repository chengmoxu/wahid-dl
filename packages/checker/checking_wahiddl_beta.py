import os
from packages.core import info
wahiddl_beta_folder_name = "wahid-dl (Beta)"
def folder():
    if info.platform() == "Windows":
        path = os.path.join("C:\\", "wahid-dl (Beta)")
    elif info.platform() == "Linux":
        path = os.path.expanduser("~/wahid-dl (Beta)")
    else:
        return False
    try:
        wahiddl_beta_folder_existed = os.path.exists(path)
        return wahiddl_beta_folder_existed
    except:
        return False