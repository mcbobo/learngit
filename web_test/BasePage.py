# coding:utf-8
from time import sleep
import datetime

class Page():
    '''页面基础类'''

    # 初始化
    def __init__(self, dirver):
        self.base_url = 'http://test.gytycn.com/zmpt_system_manage/index.php/Home'
        self.driver = dirver
        self.timeout = 10

    # 打开不同的子页面
    def _open(self, url):
        url_ = self.base_url + url
        print("Test page is： %s" % url_)
        # self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        assert self.driver.current_url == url_, 'Did ont land on %s' % url_

    def open(self):
        self._open(self.url)

    def get_statr_time(self, time_delay):
        now = datetime.datetime.now() + datetime.timedelta(minutes=time_delay)
        hm = '%s:%s' % (now.hour, now.minute)
        return hm

    # 元素定位方法封装
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

