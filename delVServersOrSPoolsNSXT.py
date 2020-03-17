import json, requests, sys
from requests.auth import HTTPBasicAuth

# Type "vs" if you'd like to delete Virtual Servers or type "sp" if you'd like to delete Server Pools
if sys.argv[1] == "vs":
  url = 'https://nsxturl/api/v1/loadbalancer/virtual-servers/'
elif sys.argv[1] == "sp":
  url = 'https://nsxturl/api/v1/loadbalancer/pools/'
else:
    print('Type "vs" if you\'d like to delete Virtual Servers or type "sp" if you\'d like to delete Server Pools')

username = 'admin'
password = 'password'

# Save data from response in the file
r = requests.get(url, verify=False, auth=HTTPBasicAuth(username, password))
with open('data.json', 'wb') as f:
    f.write(r.content)

# Save data in variable from the file
with open('data.json') as f:
  data = json.load(f)

# Parse data and delete virtual servers or server pools  
for i in data['results']:
# if i['ip_address'] == "1.2.3.4":  For example you can parse objects by ip
  requests.delete(url + i['id'], verify=False, auth=HTTPBasicAuth(username, password))
