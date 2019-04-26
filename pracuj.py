import requests
from bs4 import BeautifulSoup, NavigableString
from pprint import pprint
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
for x in range(1,177):
    url ='https://www.pracuj.pl/praca/Warszawa'+str(x)
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text,'html.parser')
    tables = []
    regon = []
    nip = []
    ulica = []
    rows = soup.findAll("li", {"class": "o-list_item"})
    for row in rows:
        rowt = str(row)
        soutds = BeautifulSoup(rowt,'html.parser')
        for td in soutds:
            tdss = BeautifulSoup(str(td),'html.parser')
            listitems = tdss.findAll("a", {"class":"o-list_item_link_name"})
            listitems = BeautifulSoup(str(listitems), 'html.parser')
            listitemshref = BeautifulSoup(str(listitems), 'html.parser')
            for a in listitemshref.find_all('a', href=True):
                listitemshref = str(a['href'])
            listitems = listitems.text.replace("[","").replace("]","").strip()
            emplo = tdss.findAll("h3", {"class":"o-list_item_link"})
            emplo = BeautifulSoup(str(emplo), 'html.parser')
            emplos = emplo.text.replace("[","").replace("]","").replace("\n","")
            loc = tdss.findAll("span",{"class":"o-list_item_desc_location"})
            for locs in loc:
                loct = locs.text.strip()
            date = tdss.findAll("span",{"class":"o-list_item_desc_date"})
            for dates in date:
                dates = dates.text.strip()
            print('"'+listitems+'","https://pracuj.pl'+listitemshref+'"'+',"'+emplos+'","'+loct+'","'+dates+'"')