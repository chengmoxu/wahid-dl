import os
from packages.checking import checking_system_os
wahiddl_folder_name = "wahid-dl"
def checking_wahiddl_folder_existed():
    if checking_system_os.get_system_os() == "Windows":
        path = os.path.join("C:\\", "wahid-dl")
    elif checking_system_os.get_system_os() == "Linux":
        path = os.path.expanduser("~/wahid-dl")
    else:
        return False, "Unsupported OS"
    try:
        wahiddl_folder_existed = os.path.exists(path)
        return wahiddl_folder_existed, None
    except Exception as error:
        return False, str(error)