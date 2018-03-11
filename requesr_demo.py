import requests
import json

#url = 'http://www.ttplus.cn'
# # #获取链接
# response = requests.get(url)
#
# #处理
# print('>>>>>>Response Headers')
# print(response.headers)
#
# print('>>>>>>Response Body')
# print(response.text)
#
#
# #发送请求
# params = {'param1': 'hello', 'param2':'world'}
# response2 = requests.get(url,params=params)
#
# #处理
# print('>>>>>>Response Headers')
# print(response2.headers)
#
#
# print('>>>>>>Response Body')
# print(response2.text)
#
# print('>>>>>>status_code')
# print(response2.status_code)
# print(response2.reason)


#处理json
r = requests.get('https://github.com/timeline.json')
print(r.json()['documentation_url'])
