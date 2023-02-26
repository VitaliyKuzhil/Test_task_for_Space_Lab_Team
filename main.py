from bs4 import BeautifulSoup
import requests

url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Парсимо таблицю з класом 'wikitable'
tag = soup.find('table', {'class': 'wikitable'})
table_body = tag.find('tbody')
tr = list(table_body.find_all('tr'))

countrys_list = list()

# Розпаковуємо рядки отриманої таблиці
for element in range(1, len(tr)):
    td = tr[element].find_all('td')

    country, full_country_name, flag_url, count_country_name = 0, 0, 0, 0
    for i in range(1, 5):
        if i == 1:
            flag_url = td[i].find('img').get('src')
        elif i == 2:
            country = td[i].text.strip()
        elif i == 3:
            full_country_name = td[i].text.strip()
        else:
            count_country_name = len(full_country_name.split())

            # Заповнюємо список зібраними словниками на кожній ітерації циклу
            countrys_list.append({'country': country, 'full_country_name': full_country_name,
                                  'flag_url': flag_url, 'count_country_name': count_country_name})


# Функція підрахунку кількості країн з тією ж
# початковою літерою, що і вказана користувачем країна
def CountTheSameStartLetter(required_country):
    counter = 0
    for j in countrys_list:
        if required_country.startswith(j['country'][0]):
            counter += 1
    return counter


# Функція друку зібраного словника з потрібною країною
def PrintCountryInfo(required_country):
    country_info = 0
    for name in countrys_list:
        if name['country'] == required_country:
            country_info = name

            # Виклик функції підрахунку кількості країн з тією ж початковою літерою
            country_info['same_letter_count'] = CountTheSameStartLetter(required_country)
    print(f'All information of input Country: {country_info}')


# Виклик функції друку результату
PrintCountryInfo(input('Input Country Name: '))
