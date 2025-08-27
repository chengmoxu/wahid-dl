import os
import shutil
from packages.core import path #unified path function
from packages.core import url #unified url function
def installer_wahiddl_DEV_install():
    os.chdir (path.wahiddl_DEV_folder())
    os.system ('curl -L -o updates.zip ' + url.wahiddl_DEV_branch())
    updates_folder_name = 'updates'
    try:
        os.mkdir (updates_folder_name)
        print (f"{updates_folder_name} 更新資料之暫存資料夾已建立")
    except:
        print (f"{updates_folder_name} 更新資料之暫存資料夾已存在")
    print ('解壓縮 wahid-dl Develop Channel 更新資料')
    os.system ('tar -zxvf updates.zip -C "C:\\wahid-dl DEV\\updates"')
    wahiddl_DEV_updatesfiles_folder = 'C:\\wahid-dl DEV\\updates\\wahid-dl-develop\\'
    for item in os.listdir(wahiddl_DEV_updatesfiles_folder):
        s = os.path.join(wahiddl_DEV_updatesfiles_folder, item)
        d = os.path.join(path.wahiddl_DEV_folder(), item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    shutil.rmtree('C:\\wahid-dl DEV\\updates')
    os.remove('C:\\wahid-dl DEV\\updates.zip')
    os.remove('C:\\wahid-dl DEV\\.gitignore')
    os.remove('C:\\wahid-dl DEV\\wahid-dl-colab.ipynb')