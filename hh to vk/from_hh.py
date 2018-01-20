import requests


response = requests.get('https://api.hh.ru/vacancies?area=1180')
content = response.json()
for number, item in enumerate(content['items'], 1):
    print('Адрес страницы: {}'.format(item['alternate_url']))
    print('Требуется: {}'.format(item['name']))
    print('Организация: {}'.format(item['employer']['name']))
    print('Обязанности: {}'.format(item['snippet']['responsibility']))
    print('Требования: {}'.format(item['snippet']['requirement']))
    if item['salary']:
        print('Зарплата: {} - {} {} {}'.format(
            item['salary']['from'],
            item['salary']['to'],
            item['salary']['currency'],
            'до вычета НДФЛ' if item['salary']['gross'] else 'на руки',
        ))
    print('-'*120)