import bs4
import requests

res = requests.get('http://www.smd.tech')

print(res.status_code)
print(res.raise_for_status())

myfile = open('Automation\\files\\smdtech.txt', 'wb')

for chunk in res.iter_content(100000):
    myfile.write(chunk)
    
print(myfile)
myfile.close()

def aboutSite(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#whatWeDo > div > div > div > p:nth-child(1)')   
    response = elems[0].text.strip()
    return response

print(aboutSite('http://www.smd.tech'))