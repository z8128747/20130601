import requests


def phone_info():

    url= 'http://127.0.0.1:5000//api/buy'
    data = {'username':'POS'}
    res = requests.post(url=url,data=data)
    print(res.json())


if __name__ == '__main__':
    phone_info()