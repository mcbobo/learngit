# coding=utf-8
import time
from appium import webdriver
from test1 import get_element

# # def setup():
# cmd1 = "appium -a 127.0.0.1 -p 4723 –U 621MECQE3E3HU --no-reset"
# os.system(cmd1)

# appium -a 127.0.0.1 -p 4723  –U  6207febc --no-reset  设置appium环境

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'Q71'
desired_caps['app'] = 'com.zhimengsports.zmpt'
desired_caps['appActivity'] = 'org.cocos2dx.javascript.AppActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)
friend_element = r'D:\obj.png'
pos = get_element(friend_element, driver)
time.sleep(2)
driver.tap([pos], 100)
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

driver.quit()
