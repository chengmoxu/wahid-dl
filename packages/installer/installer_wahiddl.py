import os
import glob
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
        wahiddl_dst_folder = 'C:\\wahid-dl\\'
        wahiddl_bat_files = glob.glob (wahiddl_updatesfiles_folder + "*.bat")
        for wahiddl_bat_file in wahiddl_bat_files:
            shutil.move (wahiddl_bat_file, wahiddl_dst_folder)
        wahiddl_py_files = glob.glob (wahiddl_updatesfiles_folder + "*.py")
        for wahiddl_py_file in wahiddl_py_files:
            shutil.move (wahiddl_py_file, wahiddl_dst_folder)
        wahiddl_updates_file_path = 'C:\\wahid-dl\\updates.zip'
        if os.path.isfile (wahiddl_updates_file_path) == True:
            os.remove (wahiddl_updates_file_path)
            print (f"更新資料 '{wahiddl_updates_file_path}' 已刪除")
        else:
            print (f"更新資料 '{wahiddl_updates_file_path}' 已不存在")
        if os.path.exists (updates_folder_name):
            shutil.rmtree (updates_folder_name)
            print (f"更新資料之暫存資料夾 '{updates_folder_name}' 已刪除")
        else:
            print (f"更新資料之暫存資料夾 '{updates_folder_name}' 已不存在")
    else:
        print ('Internal Error')
        error_location = 'installer_wahiddl_install()'
        return error_location