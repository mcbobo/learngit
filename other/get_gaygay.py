from selenium import webdriver
import time, datetime, threading
from selenium.common.exceptions import NoSuchFrameException


class GetMate():
    def __init__(self, url):
        self.driver = webdriver.Firefox()
        self.url = url
        self.driver.get(self.url)
        # self.driver.set_window_size('400','400')

    def login(self):
        self.driver.get(self.url)
        if self.driver.find_element_by_css_selector('#top-index-loginUrl'):
            self.driver.find_element_by_class_name('product-button02').click()
            time.sleep(2)
            self.driver.find_element_by_css_selector('.qqLogin_bigIco').click()
            self.driver.implicitly_wait(5)
            try:
                self.driver.switch_to.frame("ptlogin_iframe")
                self.driver.find_element_by_css_selector('.face').click()
            except NoSuchFrameException as msg:
                print(msg)
        else:
            print('账号已登录')

    def buy_on_time(self, buytime):
        self.driver.find_element_by_css_selector("[title='6GB+128GB']").click()
        self.driver.find_element_by_css_selector("[alt='银钻灰'']").click()
        while True:
            now = datetime.datetime.now()
            if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
                while True:
                    try:
                        if self.driver.find_element_by_css_selector('.product-button02').click():
                            # self.driver.find_element_by_css_selector('.product-button02').click()
                            if self.driver.find_element_by_link_text('去结算'):
                                self.driver.find_element_by_link_text('去结算').click()
                                self.driver.find_element_by_css_selector("[seed='cart-pay'']").click()
                            else:
                                time.sleep(0.1)
                    except:
                        time.sleep(0.1)
            time.sleep(0.1)


def run(url, buytime):
    run = GetMate(url)
    run.login()
    run.buy_on_time(buytime)
    # try:
    #     run.login()
    #     run.buy_on_time()
    # except:
    #     print('登录失败')
    #     run.driver.get(url)
    #     run.buy_on_time(buytime)


def threadingGo(num, url, buytime):
    while num > 0:
        name = threading.Thread(target=run, args=(url, buytime))
        name.start()
        num -= 1


url = 'https://www.vmall.com/product/357339492.html'
buytime = "2017-11-23 10:07:00"
threadingGo(5, url, buytime)
