import os
import glob
import shutil
def uninstaller_wahiddl_uninstall():
    os.chdir ("C:\\wahid-dl")
    wahiddl_old_bat_files = glob.glob ("*.bat")
    for bat_file in wahiddl_old_bat_files:
        if os.path.exists (bat_file):
            os.remove (bat_file)
            print (f"已刪除 wahid-dl 舊版的{bat_file}")
        else:
            print ("不存在 wahid-dl 舊版之 .bat 檔案")
    wahiddl_old_py_files = glob.glob ("*.py")
    for py_file in wahiddl_old_py_files:
        if os.path.exists (py_file):
            os.remove (py_file)
            print (f"已刪除 wahid-dl 的{py_file}")
        else:
            print ("不存在 wahid-dl 之 .py 檔案")
    if os.path.exists ("C:\\wahid-dl\\packages"):
        shutil.rmtree("C:\\wahid-dl\\packages")
        print (f"已刪除 wahid-dl 的 packages")
    elif not os.path.exists ("C:\\wahid-dl\\packages"):
        shutil.rmtree("C:\\wahid-dl\\packages")
        print (f"已不存在 wahid-dl 的 packages")
    if os.path.exists ("C:\\wahid-dl\\bat"):
        shutil.rmtree("C:\\wahid-dl\\bat")
        print (f"已刪除 wahid-dl 的早期版本支援")
    elif not os.path.exists ("C:\\wahid-dl\\bat"):
        shutil.rmtree("C:\\wahid-dl\\bat")
        print (f"已不存在 wahid-dl 的早期版本支援")
    if os.path.exists ("C:\\wahid-dl\\tool"):
        shutil.rmtree("C:\\wahid-dl\\tool")
        print (f"已刪除 wahid-dl 的安裝檔打包工具資料夾")
    elif not os.path.exists ("C:\\wahid-dl\\tool"):
        shutil.rmtree("C:\\wahid-dl\\tool")
        print (f"已不存在 wahid-dl 的安裝檔打包工具資料夾")