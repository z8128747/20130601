"""
  封装关键字驱动类，封装常用的接口测试方法

"""

import requests

from api_test.api_test3.conf import read_conf


class Api_keys:
    # get
    def do_get(self, path=None, headers=None, params=None, **kwargs):
        # url的组成是url+path
        url = self.set_url(path)
        requests.get(url=url, headers=headers, params=params, **kwargs)

    def set_url(self, path=None):
        # 读取配置文件的环境信息
        url = read_conf.read('servers', 'DEV')
        if path:
            url = url + path
        return url
