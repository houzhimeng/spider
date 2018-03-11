import requests


#传递参数
# def getHtmlText(url):
#     headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Mobile Safari/537.36'}
#     payload = {'wd': '侯志蒙', 'rn': '100'}
#     respones = requests.get(url, headers=headers,params=payload)
#     print(respones.url)

# getHtmlText('http://www.baidu.com/s')

#访问内容,获取编码
# headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Mobile Safari/537.36'}
# respones = requests.get('http://www.ttplus.cn', headers=headers)
# print(respones.text)
# print(respones.encoding)
# print(respones.headers)
# print(respones.status)

#获取json接口
headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Mobile Safari/537.36'}
respones1 = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=122.88.60.28')
print(respones1.json()['data'],['country'])