import os
import glob
import shutil
from packages.core import path #unified path function
def uninstaller_wahiddl_DEV_uninstall():
    os.chdir (path.wahiddl_DEV_folder())
    wahiddl_DEV_old_bat_files = glob.glob ("*.bat")
    for bat_file in wahiddl_DEV_old_bat_files:
        try:
            os.remove (bat_file)
            print (f"已刪除 wahid-dl Develop Channel 舊版的{bat_file}")
        except:
            print ("不存在 wahid-dl Develop Channel 舊版之 .bat 檔案")
    wahiddl_DEV_old_py_files = glob.glob ("*.py")
    for py_file in wahiddl_DEV_old_py_files:
        try:
            os.remove (py_file)
            print (f"已刪除 wahid-dl Develop Channel 舊版的{py_file}")
        except:
            print ("不存在 wahid-dl Develop Channel 舊版之 .py 檔案")
    try:
        shutil.rmtree(path.wahiddl_DEV_packages())
        print ("已刪除 wahid-dl Develop Channel 舊版的 packages")
    except:
        print ("已不存在 wahid-dl Develop Channel 舊版的 packages")
    try:
        shutil.rmtree(path.wahiddl_DEV_bat())
        print ("已刪除 wahid-dl Develop Channel 的早期版本支援")
    except:
        print ("已不存在 wahid-dl Develop Channel 的早期版本支援")
    try:
        shutil.rmtree(path.wahiddl_DEV_tool())
        print ("已刪除 wahid-dl Develop Channel 的安裝檔打包工具資料夾")
    except:
        print ("已不存在 wahid-dl Develop Channel 的安裝檔打包工具資料夾")
    try:
        os.remove (path.wahiddl_DEV_readme())
        print ("已刪除 README.md")
    except:
        print ("已不存在 README.md")