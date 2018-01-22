import vk
from from_hh import get_vacancies

# https://oauth.vk.com/authorize?client_id=6342720&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=wall&response_type=token&v=5.71&state=27

session = vk.Session(access_token='96db4c4d58628a8da03b6df499b1ee1202208e2e0d7637a6b2fbc6f49655442bbed64e7e4d4296db236d6')
api = vk.API(session)
# print(api.users.get(user_ids=122055741))
message = get_vacancies()
api.wall.post(owner_id='-115530976', from_group=1, message=message)