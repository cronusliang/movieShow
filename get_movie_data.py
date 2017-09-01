import json

import requests

def get_theaters():

    '''https://api.douban.com/v2/movie/in_theaters?apikey=0b2bdeda43b5688921839c8ecb20399b&city=%E5%8C%97%E4%BA%AC&start=0&count=100&client=&udid='''

    theaters_url = 'https://api.douban.com/v2/movie/in_theaters'
    param  = {'apikey':'0b2bdeda43b5688921839c8ecb20399b', 'city':'%E5%8C%97%E4%BA%AC','start':'0','count':'10','client':'','udid':''}

    r = requests.get (theaters_url, params = param)
    if r.status_code == requests.codes.ok:
        print r.content

get_theaters()


