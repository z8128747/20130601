'''



'''

from selenium import webdriver

import time


from xiang_mu_shi_zhan.P01.log2 import test_log2

log=test_log2()
# 构建浏览器对象，基于type_参数，构建对应的浏览器对象
def open_brower(type_):
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    try:

        driver = getattr(webdriver, type_)(options=options)
    except:
        driver = webdriver.Chrome()
    return driver


class Keys:

    def __init__(self, type_):
        self.driver = open_brower(type_)
        self.driver.implicitly_wait(5)

    # 打开网址
    def open(self, url):
        try:

            self.driver.get(url)
            log.info(f'打开网址{url}')
        except Exception as e:
            log.error(f'打开网址{url}失败 {e}')
    # 输入
    def input(self, by, value, text):
        try:

            self.driver.find_element(by, value).send_keys(text)
            log.info(f'通过{by}={value}，输入{text}')
        except Exception as e:
            log.error(f'元素定位失败{e}')

    # 点击
    def click(self, by, value):
        try:

            self.driver.find_element(by, value).click()
            log.info(f'通过{by}={value}点击成功')
        except Exception as e:
            log.error(f'通过{by}={value}点击失败')

    # 等待
    # def sleep(self, time_):
    #     self.time.sleep(int(time_))

    def sleep(self, time_):
        try:

            time.sleep(int(time_))
            log.info(f'强制等待{time_}秒')
        except  Exception as e:
            log.error(f'强制等待{time_}秒失败,失败原因{e}')

    # 元素定位

    def locate(self, by, value):
        try:

            return self.driver.find_element(by, value)
            log.info(f'通过{by}={value}查找元素成功')
        except Exception as e:
            log.error(f'通过{by}={value}查找元素失败,失败原因{e}')

    def quit(self):
        try :

            self.driver.quit()
            log.info('退出浏览器成功')
        except Exception as e:
            log.error(f'退出浏览器失败，失败原因{e}')
    def assert_text(self, by, value, expected):
        try:
            reality = self.locate(by, value).text
            assert reality == expected, f'实际结果{reality}与预期结果{expected}不相等'
        except Exception as e:
            print(f'元素定位失败{e}')

    def assert_almost_equal(self, by, value, expected):
        try:
            reality = self.locate(by, value).text
            assert expected in reality, f'{reality}与{expected}不相等'
            return True
        except:
            return False


if __name__ == '__main__':
    key = Keys('Chrome')
    key.open('http://baidu.com')
    key.input('id','kw','ao')
    key.click('id','su1')
    key.sleep(5)
    text=key.locate('xpath','//*[@id="s_tab"]/div/a[9]').text
    print(text)
    key.quit()

