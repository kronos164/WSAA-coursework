import csv
import requests
import json
import os

# Function to read the CSV file from a URL
def read_csv(url):
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines())
    data = list(reader)
    return data

# Dump the data in a json file in a specific folder
def dump_json(data, folder_path):
    file_path = os.path.join(folder_path, 'cso.json')
    with open(file_path, 'w') as f:
        json.dump(data, f)
        
def main():
    url = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/CSV/1.0/en'
    data = read_csv(url)
    dump_json(data, folder_path='./WSAA-coursework/assignments/')

if __name__ == "__main__":
    main()