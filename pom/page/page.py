from pom.key.key import Keys


# 百度页面
class Baidu_page(Keys):
    url = 'http://www.baidu.com'

    def search_text(self, text):
        self.open(self.url)
        self.input('id', 'kw', text)
        self.click('id', 'su')
        self.wait(3)
        self.quit()


if __name__ == '__main__':

    bd=Baidu_page('Chrome')
    bd.search_text('你好')
