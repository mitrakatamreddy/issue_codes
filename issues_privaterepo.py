import requests
import json

payload = {'access_token' : 'c625a175df66662ec300f1d4b30ce3864a992cbf'}
url = 'https://api.github.com/repos/Hacklone/private-bower/issues'

r = requests.get(url,params = payload)
print r.json()
print r.text