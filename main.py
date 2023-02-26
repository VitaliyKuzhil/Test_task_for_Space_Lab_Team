from bs4 import BeautifulSoup
import requests

url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

tag = soup.find('table', {'class': 'wikitable'})
table_body = tag.find('tbody')
tr = list(table_body.find_all('tr'))

countrys_list = list()

for element in range(1, len(tr)+1):
    td = tr[element].find_all('td')
    country, full_country_name, flag_url = 0, 0, 0
    for i in range(1, 5):
        if i == 1:
            flag_url = td[i].find('img').get('src')
        elif i == 2:
            country = td[i].text.strip()
        elif i == 3:
            full_country_name = td[i].text.strip()
        else:
            countrys_list.append({'country': country, 'full_country_name': full_country_name, 'flag_url': flag_url})

print(countrys_list)
