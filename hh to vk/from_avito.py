import requests
import time
from bs4 import BeautifulSoup

AVITO_URL = 'https://www.avito.ru'


def get_vacancies():
    response = requests.get('{}{}'.format(AVITO_URL, '/neryungri/vakansii'))
    html_doc = response.content
    soup = BeautifulSoup(html_doc, 'html.parser')
    time.sleep(2)
    tags = []
    vacancy_list = ['Свежие вакансии Нерюнгри на AVITO.RU\n🔻 🔻 🔻\n']
    for link in soup.find_all('a', class_='item-description-title-link'):
        vacancy_url = (link['href'])
        response = requests.get('{}{}'.format(AVITO_URL, vacancy_url))
        html_doc = response.content
        soup = BeautifulSoup(html_doc, 'html.parser')
        vacancy_list.append('{}{}'.format(AVITO_URL, vacancy_url))
        title = soup.find('span', class_='title-info-title-text')
        if title:
            vacancy_list.append(title.string)
            tags.append('#' + '_'.join(title.string.split()))
        seller = soup.find('div', class_='seller-info-name')
        if seller:
            vacancy_list.append(seller.a.string.strip())
            tags.append('#' + '_'.join(seller.a.string.strip().split()))
        price = soup.find('span', class_='price-value-string')
        if price:
            vacancy_list.append(str(price.contents[0].strip()))
        vacancy_list.append('')
        time.sleep(2)
    vacancy_list.append(
        '#avito #работа #Нерюнгри #вакансия #вакансии #требуется #объявления #зарплата' + ' ' + ' '.join(tags))
    return '\n'.join(vacancy_list)


# print(get_vacancies())
