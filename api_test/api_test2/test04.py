import requests
import pytest
import jsonpath


def test_01():
    url = 'www.baidu.com'
    data = {'username': 'admin', 'password': 123456}
    res = requests.post(url=url, data=data)
    sjmsg=jsonpath.jsonpath(res.json(), '$..msg')[0]
    assert 'success' == sjmsg