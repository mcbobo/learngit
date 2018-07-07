# coding:utf-8
from selenium import webdriver
import unittest
from random import choice
from time import sleep


class TestCreateGoods(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(10)
        # self.driver.set_window_size(1920, 1080)
        self.driver.set_window_size(1120, 550)
        url = r'http://test.gytycn.com/zmpt_system_manage/index.php/Home/TicketShop/index.html'
        self.driver.get(url)

    def test_create_goods(self):
        driver = self.driver
        "随机什么爱疯、ipad、手机、金币....."
        goodsSeq = [x for x in range(70201, 70228)]
        goods_id = choice(goodsSeq)
        driver.find_element_by_xpath("/html/body/div/div[1]/form/div/button[2]").click()
        driver.find_element_by_id("addGoodsNum").send_keys("5")
        driver.find_element_by_id("addGoodsCost").send_keys("100")
        driver.find_element_by_id("addGoodsSid").send_keys(goods_id)
        driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div/div[3]/button[1]').click()
        sleep(5)

    def tearDown(self):
        driver = self.driver
        driver.quit()


if __name__ == '__main__':
    unittest.main()
