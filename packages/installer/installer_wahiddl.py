import os
import shutil
def installer_wahiddl_install():
    os.chdir ('C:\\wahid-dl')
    os.system ('curl -L -o updates.zip https://codeload.github.com/chengmoxu/wahid-dl/zip/refs/heads/main')
    updates_folder_name = 'updates'
    if not os.path.exists (updates_folder_name):
        os.mkdir (updates_folder_name)
        print (f"{updates_folder_name} 更新資料之暫存資料夾已建立")
    elif os.path.exists (updates_folder_name):
        print (f"{updates_folder_name} 更新資料之暫存資料夾已存在")
    print ('解壓縮 wahid-dl 更新資料')
    os.system ('tar -zxvf updates.zip -C "C:\\wahid-dl\\updates"')
    wahiddl_updatesfiles_folder = 'C:\\wahid-dl\\updates\\wahid-dl-main\\'
    wahiddl_folder = 'C:\\wahid-dl\\'
    for item in os.listdir(wahiddl_updatesfiles_folder):
        s = os.path.join(wahiddl_updatesfiles_folder, item)
        d = os.path.join(wahiddl_folder, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    shutil.rmtree('C:\\wahid-dl\\updates')
    os.remove('C:\\wahid-dl\\updates.zip')
    os.remove('C:\\wahid-dl\\.gitignore')
    os.remove('C:\\wahid-dl\\wahid-dl-colab.ipynb')