import requests
from bs4 import BeautifulSoup

#tady ukradnu url
url = 'https://www.lavdis.cz/stavy-vodoctu/ridici-vodocty/vodocet-melnik'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')

header_row = table.find('thead').find('tr')
headers = [th.text.strip() for th in header_row.find_all('th')]

data_rows = table.find('tbody').find_all('tr')

datum_data = []
vyska_data = []
q_data = []

for row in data_rows:
    cells = row.find_all('td')
    data = [cell.text.strip() for cell in cells]
    datum_data.append(data[0])
    vyska_data.append(data[1])
    q_data.append(data[2])

#TADY vypíšu stav vody a datum
for datum, vyska, q in zip(datum_data, vyska_data, q_data):
    print("Stav vody na Mělníku v", datum, "je", vyska, "cm.")
    print()
