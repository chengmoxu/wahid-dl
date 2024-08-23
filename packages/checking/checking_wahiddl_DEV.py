import os
wahiddl_DEV_folder_name = 'wahid-dl DEV'
def checking_wahiddl_DEV_folder_existed():
    os.chdir ('C:\\')
    if os.path.exists (wahiddl_DEV_folder_name):
        wahiddl_DEV_folder_existed = 'True'
        return wahiddl_DEV_folder_existed
    elif not os.path.exists (wahiddl_DEV_folder_name):
        wahiddl_DEV_folder_existed = 'Flase'
        return wahiddl_DEV_folder_existed
    else:
        wahiddl_DEV_folder_existed = 'Internal Error'
        error_location = 'checking_wahiddl_DEV_folder_existed()'
        return wahiddl_DEV_folder_existed, error_location