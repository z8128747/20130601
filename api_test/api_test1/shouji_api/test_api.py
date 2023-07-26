import os

import allure
import requests
import pytest
from api_test.api_test1.read_yaml.read_yaml import read_yaml_file


@pytest.mark.parametrize('data', read_yaml_file('../data/phone.yaml'))
@allure.title('手机接口1')
@allure.step('手机接口')
def test_phone_api(data):
    with allure.step('发送请求'):
        r = requests.get('http://sellshop.5istudy.online/sell/shouji/query', params=data)
    # print(r.text)
    # print(r.json()['msg'])
    with allure.step('断言'):
        assert 'ok' == r.json()['msg']

# def test_phone_api2():
#     with allure.step('发送请求'):
#         r =requests.get()


if __name__ == '__main__':
    pytest.main(['--alluredir', './result','--clean-alluredir',  '--allure-no-capture'])
    # 执行命令行的命令
    os.system('allure generate ./result/ -o ./report_allure/ --clean')