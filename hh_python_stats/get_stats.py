import requests
from pprint import pprint


def get_hh_python_stats():

    vacancy_id_list = []
    skills_dict = {}
    page = 1

    while True:
        with requests.get('https://api.hh.ru/vacancies?text=Python&search_field=name&search_period=1&per_page=100&page={}'.format(page)) as response:
            content = response.json()
            if not len(content['items']):
                break
            page += 1

        for item in content['items']:
            if item['id'] not in vacancy_id_list:
                vacancy_id_list.append(item['id'])
                with requests.get(item['url']) as response:
                    content = response.json()
                    for skill in content['key_skills']:
                        skill = skill['name'].lower()
                        if skill != 'python':
                            try:
                                skills_dict[skill] += 1
                            except KeyError:
                                skills_dict.setdefault(skill, 1)
                            # print(content['description'])
    return skills_dict


if __name__ == '__main__':
    skills_dict = get_hh_python_stats()
    pprint(sorted(skills_dict.items(), key=lambda x: (x[1], x[0]), reverse=True))





