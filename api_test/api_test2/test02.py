import requests
import pytest
import jsonpath


class Test_case:
    @pytest.mark.parametrize('shouji, appkey', [['15177788888', 'a7baf0f9580e8a01']])
    def test_login(self,shouji,appkey):
        url = 'http://sellshop.5istudy.online/sell/shouji/query'
        data = {"shouji": shouji, 'appkey': appkey}
        res = requests.post(url=url, params=data)
        # print(res.json())
        sjmsg = jsonpath.jsonpath(res.json(), '$..msg')[0]
        assert 'ok' == sjmsg


if __name__ == '__main__':
    pytest.main(['-vs','test02.py'])
