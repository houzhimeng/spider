import requests
import json
from requests import  exceptions

url = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([url,endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def requests_method():
    response = requests.get(build_uri('user/emails'),auth=('houzhimeng','Hzm885649'))
    print (better_print(response.text))

def params_request():
    respones = requests.get(build_uri('users'),params={'since': 11})
    print(better_print(respones.text))
    print(respones.url)

def json_request():
    response = requests.patch(build_uri('user'),auth=('houzhimeng','Hzm885649'),json={'name':'houzhimeng', 'email': 'gleymonkey@gmial.com'})
    print(better_print(response.text))
    print(response.request.headers)
    print(response.request.body)
    print(response.status_code)

def timeout_request():
    try:
        response = requests.get(build_uri('user/emails'), timeout=10)
        response.raise_for_status()
    except exceptions.Timeout as e:
        print(e.message)
    except exceptions.HTTPError as e:
        print(e.message)
    else:
        print(response.text)
        print(response.status_code)

def hard_requests():
    from requests import Request, Session
    s = Session()
    headers = {'User-Agent': 'houzhimeng111'}
    req = Request('GET', build_uri('user/emails'),auth=('houzhimeng','Hzm885649'),headers=headers)
    prepped = req.prepare()
    print(prepped.body)
    print(prepped.headers)

    resp = s.send(prepped,timeout= 10)
    print(resp.status_code)
    print(resp.request.headers)
    print(resp.text)

if __name__ == '__main__':
    json_request()
