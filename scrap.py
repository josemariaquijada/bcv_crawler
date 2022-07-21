import requests
from bs4 import BeautifulSoup

def getExchangeRates():
  URL = "http://www.bcv.org.ve"
  r = requests.get(URL)
  soup = BeautifulSoup(r.content, 'html5lib')

  euro = soup.find(id="euro").strong.getText().strip()
  dolar = soup.find(id="dolar").strong.getText().strip()
  date = soup.find(id="dolar").parent.find(property="dc:date").attrs['content']

  response = {"date": date, "dolar": dolar, "euro": euro}
  return response


print(getExchangeRates())