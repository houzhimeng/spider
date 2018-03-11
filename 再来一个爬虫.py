import requests
import json
from http import cookiejar
import re
from bs4 import BeautifulSoup
#
# response = requests.get('http://www.ttplus.cn')
# r = response.get(url, headers={'user-agent': 'Mozilla/5.0'})
#
# #requests.get(url, headers={'user-agent': 'Mozilla/5.0'})
# print(response.status_code)
# print(response.reason)

#for name, value in response.headers.items():
#    print('%s: %s' % (name, value))

#print(response.content)
# args = { 'h': 4, "s":20}
# payload = {'key': 'value1', 'key2': 'value2'}
# response = requests.get(url="http://www.ttplus.cn", headers={'user-agent': 'Mozilla/5.0'})
# #r = requests.post("http://www.ttplus.cn", data= payload)
# print(response.url)
# print(response)

#json格式 提交数据
# url = 'http://www.ttplus.cn'
# payload = {'some': 'data'}
# r = requests.post(url, json=payload)
# print(r)


# #抓取内容，保存
# r = requests.get("https://www.javbus7.com")
# with open("test2.html","wb") as f:
#     f.write(r.content)

#处理json
# r = requests.get('https://www.v2ex.com/api/topics/hot.json')
# print(r.json())

# f = open('source', 'r')
# html = f.read()
# f.close()



headers={'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Mobile Safari/537.36'}
r = requests.get("https://www.ttplus.cn",headers=headers)
print(r.text)

