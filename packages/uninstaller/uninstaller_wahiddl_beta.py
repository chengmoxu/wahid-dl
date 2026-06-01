import os
import glob
import shutil
from packages.core import path #unified path function
def uninstall():
    os.chdir(path.wahiddl_beta_folder())
    wahiddl_beta_old_bat_files = glob.glob ("*.bat")
    for bat_file in wahiddl_beta_old_bat_files:
        try:
            os.remove (bat_file)
            print(f"已刪除 wahid-dl (Beta) 舊版的{bat_file}")
        except:
            print("不存在 wahid-dl (Beta) 舊版之 .bat 檔案")
    wahiddl_beta_old_py_files = glob.glob ("*.py")
    for py_file in wahiddl_beta_old_py_files:
        try:
            os.remove (py_file)
            print(f"已刪除 wahid-dl (Beta) 舊版的{py_file}")
        except:
            print("不存在 wahid-dl (Beta) 舊版之 .py 檔案")
    try:
        shutil.rmtree(path.wahiddl_beta_packages())
        print("已刪除 wahid-dl (Beta) 舊版的 packages")
    except:
        print("已不存在 wahid-dl (Beta) 舊版的 packages")
    try:
        shutil.rmtree(path.wahiddl_beta_bat())
        print("已刪除 wahid-dl (Beta) 的早期版本支援")
    except:
        print("已不存在 wahid-dl (Beta) 的早期版本支援")
    try:
        shutil.rmtree(path.wahiddl_beta_tool())
        print("已刪除 wahid-dl (Beta) 的安裝檔打包工具資料夾")
    except:
        print("已不存在 wahid-dl (Beta) 的安裝檔打包工具資料夾")
    try:
        os.remove (path.wahiddl_beta_readme())
        print("已刪除 README.md")
    except:
        print("已不存在 README.md")