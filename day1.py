import requests
import uuid
from bs4 import BeautifulSoup

respones = requests.get('http://www.ttplus.cn')
soup = BeautifulSoup(respones.text,'html.parser')
target = soup.find(id="m-news-list")
a = target.find_all('a')
# print(a)
filename = uuid.uuid4()


for i in a:
    img = i.find('img').attrs.get('src')
    h3 = i.find('h3').text
    print(h3)
    if img:
        imgrespons = requests.get(url=img)
        print(imgrespons.content)
        filename = h3 + '.jpg'
        with open(filename, "wb") as f:
            f.write(imgrespons.content)
    # if a:
    #     print(a.attrs.get('href'))
    #     img = a.find('img').attrs.get('src')
    #     print(img)
#
# for h in li_list:
#     h3 = h.find('h3')
#     print(h3)
# print(li_list)