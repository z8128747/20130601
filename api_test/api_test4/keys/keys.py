"""

封锁元素订单，以及浏览器的操作

"""

from selenium import webdriver
import time


# 定义一个函数启动浏览器最大化并初始化谷歌浏览器
def open_brower(type_):
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    try:
        driver = getattr(webdriver, type_)(options=options)

    except:
        driver = webdriver.Chrome()
    return driver


class Keys:

    # 初始化浏览器
    def __init__(self, type_):
        self.driver = open_brower(type_)
        self.driver.implicitly_wait(5)

    # 打开网址
    def open(self, url):
        self.driver.get(url)


    # 输入文本
    def input(self, by, value, text):
        self.driver.find_element(by, value).send_keys(text)

    # 点击
    def click(self, by, value):
        self.driver.find_element(by, value).click()

    # 等待时间
    def wait(self, time_):
        time.sleep(time_)

    # 退出浏览器
    def quit(self):
        self.driver.quit()

    # 元素定位
    def locator(self, by, value):
        el = self.driver.find_element(by, value)
        self.locater_station(el)
        return el

    # 元素定位文本
    def locator_text(self, by, value):
            self.driver.find_element(by, value).text

    # 显示定位的地方，方便确认定位位置
    def locater_station(self,element):
        self.driver.execute_script(
            "arguments[0].setAttribute('style',arguments[1]);",
            element,
            "border: 2px solid red" # 边框，red红色
        )

if __name__ == '__main__':
    key = Keys('Chrome')
    key.open('http://www.baidu.com')
    key.locator('id', 'kw').send_keys('你好')
    key.click('id', 'su')
    key.wait(3)
    key.quit()
