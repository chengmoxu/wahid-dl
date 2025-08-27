import os
import shutil
from packages.core import path #unified path function
from packages.core import url #unified url function
def installer_wahiddl_install():
    os.chdir (path.wahiddl_folder())
    os.system ('curl -L -o updates.zip ' + url.wahiddl_main_branch())
    updates_folder_name = 'updates'
    try:
        os.mkdir (updates_folder_name)
        print (f"{updates_folder_name} 更新資料之暫存資料夾已建立")
    except:
        print (f"{updates_folder_name} 更新資料之暫存資料夾已存在")
    print ('解壓縮 wahid-dl 更新資料')
    os.system ('tar -zxvf updates.zip -C "C:\\wahid-dl\\updates"')
    wahiddl_updatesfiles_folder = 'C:\\wahid-dl\\updates\\wahid-dl-main\\'
    for item in os.listdir(wahiddl_updatesfiles_folder):
        s = os.path.join(wahiddl_updatesfiles_folder, item)
        d = os.path.join(path.wahiddl_folder(), item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    shutil.rmtree('C:\\wahid-dl\\updates')
    os.remove('C:\\wahid-dl\\updates.zip')
    os.remove('C:\\wahid-dl\\.gitignore')
    os.remove('C:\\wahid-dl\\wahid-dl-colab.ipynb')