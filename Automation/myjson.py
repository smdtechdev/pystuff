import requests 

url = 'https://smd.tech/json/tester'
r = requests.get(url)
json = r.json()
print(json)