import bs4
import requests

res = requests.get('http://www.smd.tech')

print(res.status_code)
print(res.raise_for_status())

myfile = open('smdtech.txt', 'wb')

for chunk in res.iter_content(100000):
    myfile.write(chunk)
    
print(myfile)
myfile.close()    

