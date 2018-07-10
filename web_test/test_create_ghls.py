# coding:utf-8
from selenium import webdriver
import unittest
from time import sleep
import datetime
from selenium.webdriver.support.ui import Select


class TestCreatedailymtt(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        # self.driver.set_window_size(1920, 1080)
        url = r'http://test.gytycn.com/zmpt_system_manage/index.php/Home/MatchManage/societyMatch.html'
        self.driver.get(url)

    def get_statr_time(self, time_delay):
        now = datetime.datetime.now() + datetime.timedelta(minutes=time_delay)
        hm = '%s:%s' % (now.hour, now.minute)
        return hm

    def test_create_match(self):
        driver = self.driver
        sleep(2)
        driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/button[2]").click()
        match_name = datetime.datetime.now().time()
        driver.find_element_by_id("inputGoodsName").send_keys(str(match_name))
        '奖池数量'
        driver.find_element_by_id('inputGoodsNum').send_keys('1000')
        # time_delay = input('您需要几分钟后开始的比赛：')
        match_time = self.get_statr_time(time_delay=3)
        sleep(2)
        driver.find_element_by_name('beginTime').send_keys(match_time)
        driver.find_element_by_name('endTime').send_keys(match_time)
        start_date = str(datetime.datetime.now().date())
        driver.find_element_by_name('beginDate').send_keys(start_date)
        end_date = (datetime.datetime.now() + datetime.timedelta(days=1)).date()
        driver.find_element_by_name('endDate').send_keys(str(end_date))
        driver.find_element_by_id("add_people_num1").send_keys('2')
        driver.find_element_by_id("add_people_num2").send_keys('5')
        driver.find_element_by_id("add_price_num").send_keys('1000')
        driver.find_element_by_id("add_for_exit_time").send_keys('1')
        # '加购、重购次数,下拉列表'
        select = Select(driver.find_element_by_css_selector("[name='add_cgcs']"))
        select.select_by_visible_text("1")
        # select = Select(driver.find_element_by_css_selector("[name='add_jgcs']"))
        # select.select_by_visible_text("1")
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/div[11]/div[1]/div/input').send_keys(
            r'D:\OneKeyBak\backup\desktop\000.xlsx')
        # driver.find_element_by_id('save').click()
        sleep(5)

    # def tearDown(self):
    #     driver = self.driver
    #     driver.quit()


if __name__ == '__main__':
    unittest.main()
