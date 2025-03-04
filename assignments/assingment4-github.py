import requests
import json
from keys import GitHubKey as GHkey

url = 'https://api.github.com/repos/kronos164/WSAA-coursework/contents/assignments/andrewfile.json'
apikey = GHkey["GitHub-APIkey"]
folder_path='./WSAA-coursework/assignments/'
headers = {'Authorization': f'token {apikey}'}
response = requests.get(url, headers=headers)

content = response.json()
file_content = content['content']
import base64
file_content = base64.b64decode(file_content).decode('utf-8')
file_content = json.loads(file_content)
print(file_content)

file_content = json.dumps(file_content).replace('Andrew', 'Caina')
file_content = file_content.replace('Beatty', 'Oliveira')
file_content = json.loads(file_content)
print(file_content)

# Encode the modified content back to base64
updated_content = base64.b64encode(json.dumps(file_content).encode('utf-8')).decode('utf-8')

# Prepare the data for the PUT request
data = {
    'message': 'Updated file content test',
    'content': updated_content,
    'sha': content['sha']
}

response = requests.put(url, headers=headers, json=data)