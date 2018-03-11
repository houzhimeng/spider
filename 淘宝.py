import requests
import re
import json
import time
import xlwt

#地址
url = "https://s.taobao.com/search?q=%E7%8C%8E%E5%A4%A9%E4%BD%BF%E9%AD%94%E5%A5%B3&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306"
t = requests.get(url=url)
html = t.text

DATA = []

contr = re.findall(r'g_page_config = (.*?) g_srp_loadCss', html,re.S)[0].strip()[:-1]
content = json.loads(contr)
data_list = content['mods']['itemlist']['data']['auctions']
# print(data_list)

for item in data_list:
    temp = {
        'title': item['title'],
        'view_price': item['view_price'],
        'view_sales': item['view_sales'],
        'view_fee': '否' if float(item['view_fee']) else '是',
        'isTmall': '是' if float(item['shopcard']['isTmall']) else '否',
        'area': item['item_loc'],
        'name': item['nick'],
        'detail_url': item['detail_url'],
    }
    DATA.append(temp)

#保存cookie
cookies = t.cookies

#首页12条异步加载
url2 = 'https://s.taobao.com/api?_ksTS=1520091566594_238&callback=jsonp239&ajax=true&m=customized&sourceId=tb.index&q=%E7%8C%8E%E5%A4%A9%E4%BD%BF%E9%AD%94%E5%A5%B3&spm=a21bo.2017.201856-taobao-item.1&s=36&imgfile=&initiative_id=tbindexz_20170306&bcoffset=0&commend=all&ie=utf8&rn=b28a25b7bef2cf7ca0cea8723762f62c&ssid=s5-e&search_type=item'
t2 = requests.get(url=url2,cookies=cookies)
html2 = t2.text
content = re.findall(r'{.*}', html2)[0]

#格式化json
content = json.loads(content)
data_list = content['API.CustomizedApi']['itemlist']['auctions']
for item in data_list:
    temp = {
        'title': item['title'],
        'view_price': item['view_price'],
        'view_sales': item['view_sales'],
        'view_fee': '否' if float(item['view_fee']) else '是',
        'isTmall': '是' if float(item['shopcard']['isTmall']) else '否',
        'area': item['item_loc'],
        'name': item['nick'],
        'detail_url': item['detail_url'],
    }
    DATA.append(temp)
print(len(DATA))


#翻页
cookies = t2.cookies
for i in range(1, 10):
    ktsts = time.time()
    _ksts = '%s_%s' % (int(ktsts * 1000), str(ktsts)[-4:])
    callback = "jsonp%s" %(int(str(ktsts)[-4:]) + 1)
    data_value = 44 * i
    page_num = 'https://s.taobao.com/search?data-key=s&data-value={}&ajax=true&_ksTS={}&callback={}&q=%E7%8C%8E%E5%A4%A9%E4%BD%BF%E9%AD%94%E5%A5%B3&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=4&ntoffset=4&p4ppushleft=2%2C48&s=0'.format(data_value,_ksts,callback)
    t3 = requests.get(page_num, cookies=cookies)
    html = t3.text
    data_list = json.loads(re.findall(r'{.*}', html)[0])['mods']['itemlist']['data']['auctions']
    # print(data_list)

    for item in data_list:
        temp = {
            'title': item['title'],
            'view_price': item['view_price'],
            'view_sales': item['view_sales'],
            'view_fee': '否' if item['view_fee'] else '是',
            'isTmall': '是' if item['shopcard']['isTmall'] else '否',
            'area': item['item_loc'],
            'name': item['nick'],
            'detail_url': item['detail_url'],
        }
        DATA.append(temp)
print(DATA)

#画图
