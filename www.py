import requests
import re
from bs4 import BeautifulSoup
#
# html = '<div class="a">侯志蒙</div>'
# html2 = '<a href="http://www.ttplus.cn"></a>'
# #response = requests.get("http://www.ttplus.cn")
# soup = BeautifulSoup(html2,"html.parser")
# # e = soup.find('div',class_="a").text
# e = soup.find_all('a')
# for b in e:
#     link = b.get('href')
# #    print(link)
#     print ('now downloading:' + b)
#     with open("pic" + str(i),"wb") as f:
# #     f.write(pict)
#
#
# from urllib.request import urlretrieve
#
# import requests
# from bs4 import BeautifulSoup
#
# r = requests.get("http://www.pythonscraping.com")
# bs = BeautifulSoup(r.text)
# image = bs.find("a", {"id": "logo"}).find("img")["src"]
#
# urlretrieve(image, "logo.jpg")
#
#  ir = requests.get(image, stream=True)
#  if ir.status_code == 200:
#      with open('logo.jpg', 'wb') as f:
#          for chunk in ir:
#                f.write(chunk)

# import requests
# from bs4 import BeautifulSoup
#
# r = requests.get("http://www.ttplus.cn")
# bs = BeautifulSoup(r.text,'lxml')
# image = bs.find("img")["src"]
#
# ir = requests.get(image)
# if ir.status_code == 200:
#     open('logo.jpg', 'wb').write(ir.content)


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,"html.parser")
# print(soup.prettify())
# print(soup.title.string)
# print(soup.a.string)
print(soup.get_text())
# print(soup.find_all(['title','p']))
print(soup.select('body > p > a'))
# print(soup.select('p > link1'))
# print(soup.select('a[href="http://example.com/tillie"]'))


