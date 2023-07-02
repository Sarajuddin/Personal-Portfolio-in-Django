import json
from urllib.request import urlopen
try:
    url = "http://ipinfo.io/json"
    responce = urlopen(url)
    data = json.load(responce)
    print(data['ip'])
    print("------------------------------")
except:
    print("Please check your internet connection")


import requests
try:
    r = requests.get("https://get.geojs.io/")
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    ipAdd = ip_request.json()['ip']
    # print(ipAdd)
    # ipAdd = '2409:4085:881c:9277:860e:1a4a:eae:6366'
    # ipAdd = '2409:4085:868c:a071:ad45:f763:9a58:5c95'
    # ipAdd = "2409:4085:868c:a071:5d1f:cf85:56f:74b6"
    # Hritik Laptop
    # ipAdd = '2409:4085:881c:9277:199b:1125:a07f:846f'
    print(ipAdd)
    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
    print(url)
    geo_request = requests.get(url)
    print(geo_request)
    geo_data = geo_request.json()
    print(geo_data)
except:
    print("Please check your internet connection")
