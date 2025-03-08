import requests
import json

# Request the data from the url
def request(url):
    response = requests.get(url)
    data = response.json()
    return data

# Dump the data in a json file in a specific folder
def dump_json(data, folder_path):
    with open(folder_path + 'cso.json', 'w') as f:
        json.dump(data, f)
        
def main():
    url = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en'
    data = request(url)
    dump_json(data, folder_path='./WSAA-coursework/assignments/')

main()