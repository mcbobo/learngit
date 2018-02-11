# coding:utf-8
from selenium import webdriver
import unittest
from time import sleep
import datetime
from selenium.webdriver.support.ui import Select


class TestCreatedailymtt(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        url = r'http://test.gytycn.com/zmpt_system_manage/index.php/Home/MatchManage/millionMatch.html'
        self.driver.get(url)

    def get_statr_time(self, time_delay):
        now = datetime.datetime.now() + datetime.timedelta(minutes=time_delay)
        hm = '%s:%s' % (now.hour, now.minute)
        return hm

    def test_create_match(self):
        driver = self.driver
        sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/button[2]").click()
        choice = input('赛事类型（1.日赛，2.周赛，3月赛）：')
        if choice == 1:
            '日赛'
            driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div[1]/button").click()
        elif choice == 2:
            '周赛'
            driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div[2]/button").click()
        else:
            '月赛'
            driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div[3]/button").click()

        match_name = datetime.datetime.now().time()
        driver.find_element_by_id("inputGoodsName").send_keys(str(match_name))
        driver.find_element_by_id("inputGoodsNum").send_keys('1000')
        # time_delay = input('您需要几分钟后开始的比赛：')
        match_time = self.get_statr_time(time_delay=2)
        # sleep(5)
        driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/div[2]/form/div[3]/div/div[2]/input").send_keys(
            match_time)
        start_date = str(datetime.datetime.now().date())
        driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/div[2]/form/div[3]/div/div[1]/input").send_keys(
            start_date)
        # end_date = (datetime.datetime.now() + datetime.timedelta(days=1)).date()
        '可报名时间'
        driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/div[2]/form/div[4]/div/div[1]/input").send_keys(
            '1')
        driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/div[2]/form/div[5]/div/div[1]/input").send_keys(
            '2')
        driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/div[2]/form/div[6]/div/div[1]/input").send_keys(
            '2')
        driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/div[2]/form/div[6]/div/div[3]/input").send_keys(
            '5')
        driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/div[2]/form/div[8]/div/div[1]/input").send_keys(
            '2')
        driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/div[2]/form/div[9]/div/div[1]/input").send_keys(
            '20')
        # '加购、重购次数,下拉列表'
        driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/div[2]/form/div[9]/div/div[3]/input").send_keys(
            '1000')
        driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/div[2]/form/div[12]/div/div[1]/input").send_keys(
            '1000')
        # select = Select(driver.find_element_by_css_selector("[name='add_cgcs']"))
        # select.select_by_visible_text("1")
        # select = Select(driver.find_element_by_css_selector("[name='add_jgqzdj']"))
        # select.select_by_value("2")
        # select = Select(driver.find_element_by_css_selector("[name='add_jgcs']"))
        # select.select_by_visible_text("1")
        '奖励分配模式选择'
        # select = Select(driver.find_element_by_css_selector("[name='add_price_put']"))
        # select.select_by_visible_text("自定义")
        driver.find_element_by_id('create').click()
        sleep(1)

    def tearDown(self):
        driver = self.driver
        driver.quit()


if __name__ == '__main__':
    unittest.main()
