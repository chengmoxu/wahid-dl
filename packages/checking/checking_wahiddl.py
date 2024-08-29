import os
wahiddl_folder_name = 'wahid-dl'
def checking_wahiddl_folder_existed():
    os.chdir ('C:\\')
    if os.path.exists (wahiddl_folder_name):
        wahiddl_folder_existed = 'True'
        error_location = 'False'
    elif not os.path.exists (wahiddl_folder_name):
        wahiddl_folder_existed = 'Flase'
        error_location = 'False'
    else:
        wahiddl_folder_existed = 'Internal Error'
        error_location = 'checking_wahiddl_folder_existed()'
    return wahiddl_folder_existed, error_location