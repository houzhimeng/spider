import requests
post_dict = {
"phone":'8618611720843',
"password":'Hzm885649',
"oneMonth":1
}

session = requests.session()
h1 = session.get(url='https://dig.chouti.com',
                 headers={
                    'Referer': 'https://m.chouti.com/',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Mobile Safari/537.36'
                }
)

h2 = session.request(
    method='POST',
    url="https://dig.chouti.com/login",
    data=post_dict,
    headers={
        'Referer': 'https://dig.chouti.com/',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Mobile Safari/537.36'
    }
)

h3 = session.request(
    method='POST',
    url="https://dig.chouti.com/link/vote?linksId=17629711",
    headers={
        'Referer': 'https://dig.chouti.com/all/hot/recent/1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Mobile Safari/537.36'
    }
)

print(h3.text)