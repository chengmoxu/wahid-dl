# Installer Generation Tool
# [Dev] v5.3-20241116.1
import os
import sys
from pathlib import Path
def checking_wahiddl_packages_folder_existed():
    if sys.platform  == "win32":
        path = os.path.join("C:\\", "wahid-dl", "packages")
    elif sys.platform  == "linux":
        path = os.path.expanduser("~/wahid-dl/packages")
    else:
        return False, "Unsupported OS"
    try:
        wahiddl_packages_folder_existed = os.path.exists(path)
        return wahiddl_packages_folder_existed, None
    except Exception as error:
        return False, str(error)
def checking_wahiddl_tool_existed():
    try:
        wahiddl_tool_path = Path('C:/wahid-dl/wahid-dl Tool.py')
        return wahiddl_tool_path.is_file(), None     
    except Exception as error:
        return False, f"Error checking wahid-dl Tool.py: {str(error)}"