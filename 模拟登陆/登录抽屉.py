import requests
post_dict = {
"phone":'8618611720843',
"password":'hzm885649',
"oneMonth":1
}

# respones = requests.post(
#     url="https://dig.chouti.com/login",
#     data=post_dict
# )
#
# print(respones.text)https://www.javbus.com/
# cookie = respones.cookies.get_dict()
# print(cookie)

respones = requests.request(
    method='POST',
    url="https://dig.chouti.com/login",
    # params = {'k1':'v1', 'k2':'v2'},
    # json = {'use':'hou','pwd':'123'},
    data=post_dict,
    headers={
        'Referer': 'https://dig.chouti.com',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Mobile Safari/537.36'
    }
)
#获取cookie
cookies_dict = respones.cookies.get_dict()

#访问个人设置页
respones2 = requests.request(
    method='GET',
    url="https://dig.chouti.com/profile",
    cookies=cookies_dict,
    headers={
        'Referer': 'https://dig.chouti.com',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Mobile Safari/537.36'
    }
)

#提交跳票
respones3 = requests.request(
    method='POST',
    url="https://dig.chouti.com/link/vote?linksId=17631526",
    cookies={'gpsd':'29cc5aa05c920f32c1b0719455af2639'},
    headers={
        'Referer': 'https://dig.chouti.com/all/hot/recent/1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Mobile Safari/537.36'
    }
)

print(respones.text)
print(respones.cookies.get_dict())
# print(respones2.text)
print(respones3.text)
