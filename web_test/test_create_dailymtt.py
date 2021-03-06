# coding:utf-8
from selenium import webdriver
import unittest
from time import sleep
import datetime
from selenium.webdriver.support.ui import Select


class TestCreatedailymtt(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(10)
        self.driver.set_window_size(1920, 1080)
        url = r'http://test.gytycn.com/zmpt_system_manage/index.php/Home/MatchManage/index.html'
        self.driver.get(url)

    def get_statr_time(self, time_delay):
        now = datetime.datetime.now() + datetime.timedelta(minutes=time_delay)
        hm = '%s:%s' % (now.hour, now.minute)
        return hm

    def test_create_match(self):
        min_people = str(2)
        max_people = str(100)
        price_num = str(5000)
        # exit_time = str(5)
        driver = self.driver
        # sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/a").click()
        match_name = datetime.datetime.now().time()
        driver.find_element_by_id("add_match_name").send_keys(str(match_name))
        # time_delay = input('您需要几分钟后开始的比赛：')
        match_time = self.get_statr_time(time_delay=2)
        print match_time
        # sleep(5)
        driver.find_element_by_id("add_match_time").send_keys(match_time)
        start_date = datetime.date.today().strftime('%Y-%m-%d')
        driver.find_element_by_id("add_match_date").send_keys(start_date)
        end_date = (datetime.datetime.now() + datetime.timedelta(days=2)).date()
        driver.find_element_by_id("add_end_date2").send_keys(str(end_date))
        driver.find_element_by_id("add_people_num1").send_keys(min_people)
        driver.find_element_by_id("add_people_num2").send_keys(max_people)
        driver.find_element_by_id("add_price_num").send_keys(price_num)
        driver.find_element_by_id("add_for_exit_time").send_keys('3')
        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/form/div[12]/div[1]/div/input").send_keys("1")
        # '加购、重购次数,下拉列表'
        select = Select(driver.find_element_by_css_selector("[name='add_cgcs']"))
        select.select_by_visible_text("1")
        # select = Select(driver.find_element_by_css_selector("[name='add_jgqzdj']"))
        # select.select_by_value("2")
        select = Select(driver.find_element_by_css_selector("[name='add_jgcs']"))
        select.select_by_visible_text("1")
        '奖励分配模式选择'
        select = Select(driver.find_element_by_css_selector("[name='add_price_put']"))
        select.select_by_visible_text("自定义")
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/div[11]/div[1]/div/input').send_keys(
            r'D:\OneKeyBak\backup\desktop\reward\实物大奖.xlsx')
        '服务费比例'
        driver.find_element_by_id('add_service_price').send_keys('10')
        '奖励竞技分'
        # driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/div[13]/div[1]/div[2]/input[1]').clear()
        # driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/div[13]/div[1]/div[2]/input[1]').send_keys(
        #     '0')
        # driver.find_element_by_id('save').click()

    def tearDown(self):
        driver = self.driver
        driver.quit()


if __name__ == '__main__':
    unittest.main()
