import requests

BASE_URL = 'http://api.github.com'

def construct_url(end_point):
    return '/'.join([BASE_URL, end_point])


def basic_auth():
    response = requests.get(construct_url('user'),auth=('houzhimeng','Hzm885649'))
    print(response.text)
    print(response.headers)



if __name__ == "__main__":
    basic_auth()