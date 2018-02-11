from selenium import webdriver
import unittest
from  time import sleep


class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("http://test.gytycn.com/zmpt_system_manage/index.php/Home/Index")

    def test_creade_goods(self):
        driver = self.driver
        for i in range(20):
            driver.find_element_by_class_name("nav-label").click()
            driver.find_element_by_class_name("pull-left search-btn btn btn-default").click()
            driver.find_element_by_id("addGoodsNum").send_keys("5")
            driver.find_element_by_id("addGoodsCost").send_keys("100")
            driver.find_element_by_id("addGoodsSid").send_keys("70201")
            driver.find_element_by_class_name("btn btn-primary").click()
            sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
