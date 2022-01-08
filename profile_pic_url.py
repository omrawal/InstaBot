import requests


def get_profile_pic_url(uname):
    url = f'https://www.instagram.com/{uname}/?__a=1'
    resp = requests.get(url=url)
    data = resp.json()
    return (data['graphql']['user']["profile_pic_url_hd"])
