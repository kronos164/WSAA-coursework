import requests
import json
from keys import GitHubKey as GHkey
import base64

# This function reads the file from the GitHub repository through the GitHub API using a key (in this case, the key, as a Github token, is stored in the keys.py file)
def read_file(url, apikey):
    headers = {'Authorization': f'token {apikey}'}
    response = requests.get(url, headers=headers)
    content = response.json()
    file_content = content['content']
    return file_content, content

# This function decodes the content of the file from base64 and converts it to a dictionary
def decode_content(file_content):
    file_content = base64.b64decode(file_content).decode('utf-8')
    file_content = json.loads(file_content)
    return file_content

# This function encodes the content of the file back to base64
def encode_content(file_content):
    updated_content = base64.b64encode(json.dumps(file_content).encode('utf-8')).decode('utf-8')
    return updated_content

# This function replaces the names in the file for my name
def replace_content(file_content):
    file_content = json.dumps(file_content).replace('Andrew', 'Caina')
    file_content = file_content.replace('Beatty', 'Oliveira')
    file_content = json.loads(file_content)
    return file_content

# This function prepares the data for the commit
def prepare_commit(updated_content, content):
    data = {
        'message': 'Updated file content with my name',
        'content': updated_content,
        'sha': content['sha']
    }
    return data

# This function commits the changes to the file in the GitHub repository
def commit(url, headers, data):
    response = requests.put(url, headers=headers, json=data)
    return response

# This function calls all the other functions to read the file, decode the content, replace the names, encode the content, prepare the commit data and commit the changes
def main():
    url = 'https://api.github.com/repos/kronos164/WSAA-coursework/contents/assignments/andrewfile.json'
    apikey = GHkey["GitHub-APIkey"]
    headers = {'Authorization': f'token {apikey}'}
    file_content, content = read_file(url, apikey)
    file_content = decode_content(file_content)
    file_content = replace_content(file_content)
    updated_content = encode_content(file_content)
    data = prepare_commit(updated_content, content)
    response = commit(url, headers, data)
    print(response)

if __name__ == '__main__':
    main()