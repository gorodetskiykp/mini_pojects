import vk
import from_hh, from_avito
import time


# AUTH_URI = 'https://oauth.vk.com/authorize?client_id=6342720&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=wall&response_type=token&v=5.71&state=27'




session = vk.Session(access_token='1285de5330374b0160d53439a5ec617ecfb00aaf0fd600b6d0a142193a934238bce0485b90004bccfbc08')
api = vk.API(session, timeout=60)

trying = True
while trying:
    try:
        message = from_hh.get_vacancies()
        api.wall.post(owner_id='-115530976', from_group=1, message=message, attachments='photo-354372_437990310,')
        print('HH OK')
        trying = False
    except Exception as e:
        print('HH fails')
        print(e)
        time.sleep(60)

trying = True
while trying:
    try:
        message = from_avito.get_vacancies()
        api.wall.post(owner_id='-115530976', from_group=1, message=message, attachments='photo-5755934_456271122,')
        print('AVITO OK')
        trying = False
    except Exception as e:
        print('AVITO fails')
        print(e)
        time.sleep(60)
