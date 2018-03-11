import requests
from bs4 import BeautifulSoup

def getHtmlText(url):
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Mobile Safari/537.36'}
    respones = requests.get(url, headers=headers)
    soup = BeautifulSoup(respones.text, "html.parser")
    print(soup)


getHtmlText('http://www.ttplus.cn')