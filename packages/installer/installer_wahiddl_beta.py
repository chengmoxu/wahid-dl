import os
import shutil
import subprocess
from packages.core import path #unified path function
from packages.core import url #unified url function
def install():
    os.chdir(path.wahiddl_beta_folder())
    subprocess.run(['curl', '-L', '-o', 'updates.zip', url.wahiddl_beta_branch()[0]])
    updates_folder_name = 'updates'
    try:
        os.mkdir(updates_folder_name)
        print(f"{updates_folder_name} 更新資料之暫存資料夾已建立")
    except:
        print(f"{updates_folder_name} 更新資料之暫存資料夾已存在")
    print('解壓縮 wahid-dl (Beta) 更新資料')
    subprocess.run(['tar', '-zxvf', 'updates.zip', '-C', 'C:\\wahid-dl (Beta)\\updates'])
    wahiddl_beta_updatesfiles_folder = 'C:\\wahid-dl (Beta)\\updates\\wahid-dl-beta\\'
    for item in os.listdir(wahiddl_beta_updatesfiles_folder):
        s = os.path.join(wahiddl_beta_updatesfiles_folder, item)
        d = os.path.join(path.wahiddl_beta_folder(), item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    shutil.rmtree('C:\\wahid-dl (Beta)\\updates')
    os.remove('C:\\wahid-dl (Beta)\\updates.zip')
    os.remove('C:\\wahid-dl (Beta)\\.gitignore')
    os.remove('C:\\wahid-dl (Beta)\\wahid-dl-colab.ipynb')