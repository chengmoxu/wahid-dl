import os
import shutil
def installer_wahiddl_DEV_install():
    os.chdir ('C:\\wahid-dl DEV')
    os.system ('curl -L -o updates.zip https://codeload.github.com/chengmoxu/wahid-dl/zip/refs/heads/develop')
    updates_folder_name = 'updates'
    if not os.path.exists (updates_folder_name):
        os.mkdir (updates_folder_name)
        print (f"{updates_folder_name} 更新資料之暫存資料夾已建立")
    elif os.path.exists (updates_folder_name):
        print (f"{updates_folder_name} 更新資料之暫存資料夾已存在")
    print ('解壓縮 wahid-dl DEV 更新資料')
    os.system ('tar -zxvf updates.zip -C "C:\\wahid-dl DEV\\updates"')
    wahiddl_DEV_updatesfiles_folder = 'C:\\wahid-dl DEV\\updates\\wahid-dl-develop\\'
    wahiddl_DEV_folder = 'C:\\wahid-dl DEV\\'
    for item in os.listdir(wahiddl_DEV_updatesfiles_folder):
        s = os.path.join(wahiddl_DEV_updatesfiles_folder, item)
        d = os.path.join(wahiddl_DEV_folder, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    shutil.rmtree('C:\\wahid-dl DEV\\updates')
    os.remove('C:\\wahid-dl DEV\\updates.zip')
    os.remove('C:\\wahid-dl DEV\\.gitignore')
    os.remove('C:\\wahid-dl DEV\\wahid-dl.ipynb')