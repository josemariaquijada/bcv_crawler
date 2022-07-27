from copyreg import constructor
from xml.etree.ElementTree import tostring
import requests
from bs4 import BeautifulSoup
from datetime import datetime



def getExchangeRates():
  URL = "http://www.bcv.org.ve"
  r = requests.get(URL)
  today = datetime.today().strftime("%Y-%m-%d") 
    
  soup = BeautifulSoup(r.content, 'html5lib')

  euro = soup.find(id="euro").strong.getText().strip()
  dolar = soup.find(id="dolar").strong.getText().strip()
  date = soup.find(id="dolar").parent.find(property="dc:date").attrs['content']

  response = {"date": date, "dolar": dolar, "euro": euro}

  rateDate = response["date"][0:10]

  if today == rateDate:
    return response

  return "Tasa no corresponde al dia de hoy"



print(getExchangeRates())