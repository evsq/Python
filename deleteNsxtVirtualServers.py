import json
import requests
from requests.auth import HTTPBasicAuth

with open('data.json') as data_file:
    data = json.load(data_file)

for i in data['results']:
  if i['ip_address'] == "1.2.3.4":
    requests.delete('https://yournsxturl/api/v1/loadbalancer/virtual-servers/' + i['id'], verify=False, auth=HTTPBasicAuth('login', 'password'))
