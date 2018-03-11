import re
from bs4 import BeautifulSoup
import urllib.request
import requests
from urllib.request import urlretrieve


i = 0
def crawl():
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Mobile Safari/537.36'}
    respones = requests.get('https://www.toutiao.com',headers=headers)
    # print(type(r))

    soup = BeautifulSoup(respones.text, "html.parser")
    my_pic = soup.find_all('img')
    for a in my_pic:
         b = a.get('src')
         print(b)
         global i
         if respones.status_code == 200:
            urlretrieve(b,"pic" + str(i)  + ".jpg")
            i += 1

         #with open("pic" + str(i)+'.jpg', "wb") as f:
         #    f.write(b)
         #    i += 1
crawl()
