import os
import glob
def uninstaller_wahiddl_DEV_uninstall():
    os.chdir ('C:\\wahid-dl DEV')
    wahiddl_DEV_old_bat_files = glob.glob ("*.bat")
    for bat_file in wahiddl_DEV_old_bat_files:
        if os.path.exists (bat_file):
            os.remove (bat_file)
            print (f"已刪除 wahid-dl DEV 舊版的{bat_file}")
        else:
            print ("不存在 wahid-dl DEV 舊版之 .bat 檔案")
    wahiddl_DEV_old_py_files = glob.glob ("*.py")
    for py_file in wahiddl_DEV_old_py_files:
        if os.path.exists (py_file):
            os.remove (py_file)
            print (f"已刪除 wahid-dl DEV 舊版的{py_file}")
        else:
            print ("不存在 wahid-dl DEV 舊版之 .py 檔案")