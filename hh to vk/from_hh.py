import requests


response = requests.get('https://api.hh.ru/vacancies?area=1180')
content = response.json()


def get_vacancies():
    message = []
    for number, item in enumerate(content['items'], 1):
        message.append('⚠ {}'.format(item['alternate_url']))
        message.append('⚠ Требуется: {}'.format(item['name']))
        message.append('⚠ Организация: {}'.format(item['employer']['name']))
        message.append('‼ Обязанности: {}'.format(item['snippet']['responsibility']))
        message.append('‼ Требования: {}'.format(item['snippet']['requirement']))
        if item['salary']:
            message.append('⚠ Зарплата: {} - {} {} {}'.format(
                item['salary']['from'],
                item['salary']['to'],
                item['salary']['currency'],
                'до вычета НДФЛ' if item['salary']['gross'] else 'на руки',
            ))
        message.append('')
    return '\n'.join(message)

print(get_vacancies())
