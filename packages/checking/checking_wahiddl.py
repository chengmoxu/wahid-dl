import os
wahiddl_folder_name = 'wahid-dl'
def checking_wahiddl_folder_existed():
    os.chdir ('C:\\')
    if os.path.exists (wahiddl_folder_name):
        wahiddl_folder_existed = 'True'
        return wahiddl_folder_existed
    elif not os.path.exists (wahiddl_folder_name):
        wahiddl_folder_existed = 'Flase'
        return wahiddl_folder_existed
    else:
        wahiddl_folder_existed = 'Internal Error'
        error_location = 'checking_wahiddl_folder_existed()'
        return wahiddl_folder_existed, error_location