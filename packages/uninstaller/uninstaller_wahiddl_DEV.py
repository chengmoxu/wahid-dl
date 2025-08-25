import os
import glob
import shutil
from packages.core import path #unified path function
def uninstaller_wahiddl_DEV_uninstall():
    os.chdir (path.wahiddl_DEV_folder())
    wahiddl_DEV_old_bat_files = glob.glob ("*.bat")
    for bat_file in wahiddl_DEV_old_bat_files:
        if os.path.exists (bat_file):
            os.remove (bat_file)
            print (f"已刪除 wahid-dl Develop Channel 舊版的{bat_file}")
        else:
            print ("不存在 wahid-dl Develop Channel 舊版之 .bat 檔案")
    wahiddl_DEV_old_py_files = glob.glob ("*.py")
    for py_file in wahiddl_DEV_old_py_files:
        if os.path.exists (py_file):
            os.remove (py_file)
            print (f"已刪除 wahid-dl Develop Channel 舊版的{py_file}")
        else:
            print ("不存在 wahid-dl Develop Channel 舊版之 .py 檔案")
    if os.path.exists (path.wahiddl_DEV_packages()):
        shutil.rmtree(path.wahiddl_DEV_packages())
        print (f"已刪除 wahid-dl Develop Channel 舊版的 packages")
    elif not os.path.exists (path.wahiddl_DEV_packages()):
        print (f"已不存在 wahid-dl Develop Channel 舊版的 packages")
    if os.path.exists (path.wahiddl_DEV_bat()):
        shutil.rmtree(path.wahiddl_DEV_bat())
        print (f"已刪除 wahid-dl Develop Channel 的早期版本支援")
    elif not os.path.exists (path.wahiddl_DEV_bat()):
        print (f"已不存在 wahid-dl Develop Channel 的早期版本支援")
    if os.path.exists (path.wahiddl_DEV_tool()):
        shutil.rmtree(path.wahiddl_DEV_tool())
        print (f"已刪除 wahid-dl Develop Channel 的安裝檔打包工具資料夾")
    elif not os.path.exists (path.wahiddl_DEV_tool()):
        print (f"已不存在 wahid-dl Develop Channel 的安裝檔打包工具資料夾")
    if os.path.isfile (path.wahiddl_DEV_readme()) == True:
        os.remove (path.wahiddl_DEV_readme())
        print (f"已刪除 README.md")
    elif not os.path.isfile (path.wahiddl_DEV_readme()) == True:
        print (f"已不存在 README.md")