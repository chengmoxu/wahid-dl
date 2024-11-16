import os
from packages.core import system_os
wahiddl_DEV_folder_name = "wahid-dl DEV"
def checking_wahiddl_DEV_folder_existed():
    if system_os.get_system_os() == "Windows":
        path = os.path.join("C:\\", "wahid-dl DEV")
    elif system_os.get_system_os() == "Linux":
        path = os.path.expanduser("~/wahid-dl DEV")
    else:
        return False, "Unsupported OS"
    try:
        wahiddl_DEV_folder_existed = os.path.exists(path)
        return wahiddl_DEV_folder_existed, None
    except Exception as error:
        return False, str(error)