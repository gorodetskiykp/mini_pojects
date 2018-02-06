import requests


response = requests.get('https://api.hh.ru/vacancies?area=1180')
content = response.json()


def get_vacancies():
    tags = []
    message = ['Свежие вакансии Нерюнгри на HH.RU\n🔻 🔻 🔻\n']
    for number, item in enumerate(content['items'], 1):
        message.append('➡ {}'.format(item['alternate_url']))
        message.append('➡ Требуется: {}'.format(item['name']))
        message.append('➡ Организация: {}'.format(item['employer']['name']))
        tags.append('#' + '_'.join(item['name'].split()))
        tags.append('#' + '_'.join(item['employer']['name'].split()))
        if item['snippet']['responsibility']:
            message.append('‼ Обязанности: {}'.format(item['snippet']['responsibility']))
        if item['snippet']['requirement']:
            message.append('‼ Требования: {}'.format(item['snippet']['requirement']))
        if item['salary']:
            salary_from = 'от {}'.format(item['salary']['from']) if item['salary']['from'] else ''
            salary_to = ' до {}'.format(item['salary']['to']) if item['salary']['to'] else ''
            message.append('➡ Зарплата: {}{} {} {}'.format(
                salary_from,
                salary_to,
                item['salary']['currency'],
                'до вычета НДФЛ' if item['salary']['gross'] else 'на руки',
            ))
        message.append('')
    message.append('#hh #headhanter #работа #Нерюнгри #вакансия #вакансии #требуется #объявления #зарплата' + ' ' + ' '.join(tags))

    return '\n'.join(message)

# print(get_vacancies())
