import requests, json

login = 'https://example.com/api/login'
getList = 'https://example.com/api/list'
data = {'username': 'user', 'password': 'password'}

post = requests.post(login, data=json.dumps(data))
j = json.loads(post.content)
token = (j['token'])
head = {'Authorization': token}

get = requests.get(getList, headers=head)
j = json.loads(get.content)
clusterName = (j[0]['name'])
clusterId = (j[0]['id'])

getFile = requests.get('https://example.com/api/config?name={name}&clusterID={id}'.format(name=clusterName, id=clusterId), headers=head)
with open('file-{name}'.format(name=clusterName), 'wb') as file:
    file.write(getFile.content)
