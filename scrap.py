import requests
from bs4 import BeautifulSoup

URL = "http://www.bcv.org.ve"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

euro = soup.find(id="euro")
dolar = soup.find(id="dolar")

print(euro.strong.getText())
print(dolar.strong.getText())