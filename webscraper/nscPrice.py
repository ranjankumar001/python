import requests
import time
from win10toast import ToastNotifier
import webbrowser
from bs4 import BeautifulSoup

def current_price(url):
    site = requests.get(url)
    # toaster = ToastNotifier()
    # toaster.show_toast("Hello World!!!", "Python is awesome and I am learning a lot!",icon_path=None, duration=160)
    #print(site.text)
    # while toaster.notification_active(): time.sleep(0.1)
    soup = BeautifulSoup(site.text,"html.parser")
    for link in soup.find_all("span", id ="Nse_Prc_tick"):
    #   #print(link)
        name = link.getText()
        #print('current Price :',name)
        #toaster.show_toast("IDFC Bank!!!", "Current Price :"+str(name),icon_path=None, duration=30)
    return name

while True:
      toaster = ToastNotifier()
      idfc = current_price("http://www.moneycontrol.com/india/stockpricequote/banks-private-sector/idfcbank/IDF01")
      hind = current_price("http://www.moneycontrol.com/india/stockpricequote/metals-non-ferrous/hindustancopper/HC07")
      ab =   current_price("http://www.moneycontrol.com/india/stockpricequote/finance-investments/adityabirlacapital/ABC9")
      cadila = current_price("http://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/cadilahealthcare/CHC")
      mep = current_price("http://www.moneycontrol.com/india/stockpricequote/infrastructure-general/mepinfrastructuredevelopers/MID")

      rates ="IDFC Bank : " + str(idfc) + "\tHind Copper : " +str(hind) +"\nAB Capital : "+str(ab)
      rates = rates +"\nCadila Heathcare : "+str(cadila) +"\nMEP infra :"+ str(mep)
      toaster.show_toast("Price Alert!!!", rates,icon_path=None, duration=30)
      time.sleep(60)