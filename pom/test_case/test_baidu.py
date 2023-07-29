import pytest


from pom.page.page import Baidu_page
from pom.read_file.read_yaml import read_yaml


class Test_baidu_serach:

    @pytest.mark.parametrize('data', read_yaml('../data/baidu.yaml'))
    def test_01(self, data):
        page = Baidu_page('Chrome')
        page.search_text(data['text'])


if __name__ == '__main__':
    pytest.main(['-vs'])
