# coding=utf-8
import time
from appium import webdriver
from base import Appium_Extend
from capability import driver

# # def setup():
# cmd1 = "appium -a 127.0.0.1 -p 4723 –U 621MECQE3E3HU --no-reset"
# os.system(cmd1)

# appium -a 127.0.0.1 -p 4723  –U  6207febc --no-reset  设置appium环境

d = Appium_Extend(driver)
time.sleep(10)
loginv_path = r'D:\test.png'
pos = d.get_element(loginv_path)
print pos
# d.touch(loginv_path)
time.sleep(5)
# driver.close_app()
# driver.launch_app()
# driver.find_element_by_name("签到领取").click()

# driver.find_element_by_name("1").click()
#
# driver.find_element_by_name("5").click()
#
# driver.find_element_by_name("9").click()
#
# driver.find_element_by_name("删除").click()
#
# driver.find_element_by_name("9").click()
#
# driver.find_element_by_name("5").click()
#
# driver.find_element_by_name("+").click()
#
# driver.find_element_by_name("6").click()
#
# driver.find_element_by_name("=").click()

# driver.quit()
