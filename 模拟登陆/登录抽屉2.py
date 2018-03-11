import requests

#基本信息
post_dict = {
"phone":'8618611720843',
"password":'Hzm885649',
"oneMonth":1
}

#获取第一次gpsd
r1 = requests.request(
    method='GET',
    url="https://dig.chouti.com",
    headers={
        'Referer': 'https://m.chouti.com/',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Mobile Safari/537.36'
    }
)
r1_cookie = r1.cookies.get_dict()

#获取logingpsd
r2 = requests.request(
    method='POST',
    url="https://dig.chouti.com/login",
    data=post_dict,
    cookies=r1_cookie,
    headers={
        'Referer': 'https://dig.chouti.com/',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Mobile Safari/537.36'
    }
)

r2_cookie = r2.cookies.get_dict()

#登录个人设置页面
# r3 = requests.request(
#     method='GET',
#     url="https://dig.chouti.com/profile",
#     data=post_dict,
#     cookies={'gpsd':r1_cookie['gpsd']},
#     headers={
#         'Referer': 'https://dig.chouti.com',
#         'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Mobile Safari/537.36'
#     }
# )

#投票
r4 = requests.request(
    method='POST',
    url="https://dig.chouti.com/link/vote?linksId=17629711",
    cookies={'gpsd':r1_cookie.get('gpsd')},
    headers={
        'Referer': 'https://dig.chouti.com/all/hot/recent/1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Mobile Safari/537.36'
    }
)

print(r4.text)
