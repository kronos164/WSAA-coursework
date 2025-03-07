import requests
import json
from keys import GitHubKey as GHkey
import base64

def read_file(url, apikey):
    headers = {'Authorization': f'token {apikey}'}
    response = requests.get(url, headers=headers)
    content = response.json()
    file_content = content['content']
    return file_content, content

def decode_content(file_content):
    file_content = base64.b64decode(file_content).decode('utf-8')
    file_content = json.loads(file_content)
    return file_content

def encode_content(file_content):
    updated_content = base64.b64encode(json.dumps(file_content).encode('utf-8')).decode('utf-8')
    return updated_content

def replace_content(file_content):
    file_content = json.dumps(file_content).replace('Andrew', 'Caina')
    file_content = file_content.replace('Beatty', 'Oliveira')
    file_content = json.loads(file_content)
    return file_content

def prepare_commit(url, apikey, updated_content, content):
    headers = {'Authorization': f'token {apikey}'}
    response = requests.get(url, headers=headers)
    content = response.json()
    data = {
        'message': 'Updated file content test',
        'content': updated_content,
        'sha': content['sha']
    }
    return data

def commit(url, headers, data):
    response = requests.put(url, headers=headers, json=data)
    return response

def main():
    url = 'https://api.github.com/repos/kronos164/WSAA-coursework/contents/assignments/andrewfile.json'
    apikey = GHkey["GitHub-APIkey"]
    headers = {'Authorization': f'token {apikey}'}
    file_content, content = read_file(url, apikey)
    file_content = decode_content(file_content)
    file_content = replace_content(file_content)
    updated_content = encode_content(file_content)
    data = prepare_commit(url, apikey, updated_content, content)
    response = commit(url, headers, data)
    print(response)

if __name__ == '__main__':
    main()