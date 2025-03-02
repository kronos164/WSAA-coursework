import requests
import json
from keys import GitHubKey as GHkey

filename = "andrewfile.json"

url = 'https://api.github.com/repos/kronos164/WSAA-coursework/contents/assignments'


apikey = GHkey["GitHub-APIkey"]
response = requests.get(url, auth = ('token', apikey))

print (response.status_code)
print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)