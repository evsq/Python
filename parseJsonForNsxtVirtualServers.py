import json

with open('data.json') as data_file:
    data = json.load(data_file)

for i in data['results']:
  if i['ip_address'] == "1.2.3.4":
    print(i['ip_address'], i['id'])
