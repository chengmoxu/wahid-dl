import requests
def get_internet_status():
    internet_status = ''
    github_url = 'https://github.com/'
    github_response = requests.get (github_url, timeout=5)
    if github_response.status_code != 200:
        internet_status = False  
    elif github_response.status_code == 200:
        internet_status = True
    return internet_status
