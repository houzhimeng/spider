import requests

def down_image():
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Mobile Safari/537.36'}
    url = "hhttp://resource.ttplus.cn/publish/app/data/2017/05/11/54680/9f845bad-c400-4ec9-b12d-bb2c33d29271.jpg"
    response = requests.get(url,headers=headers,stream=True)
    with open('demo.jpg','wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)
            print(chunk)


down_image()

