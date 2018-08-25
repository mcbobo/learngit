# coding:utf-8
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

username = '13726221317'
pwd = 'zmjj123456'
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '127.0.0.1:21513'

# desired_caps['app'] = r'D:\weixin.apk'
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

# time.sleep(10)
# WebDriverWait(driver, 8).until(lambda x: x.find_element_by_id('com.wondershare.drfone:id/btnBackup'))
# 登录
driver.find_element_by_id('com.tencent.mm:id/d75').click()
driver.find_element_by_id('com.tencent.mm:id/hz').send_keys(username)
driver.find_element_by_id('com.tencent.mm:id/alr').click()
driver.find_element_by_id('com.tencent.mm:id/hz').send_keys(pwd)
driver.find_element_by_id('com.tencent.mm:id/alr').click()
time.sleep(10)
# WebDriverWait(driver, 8).until(lambda x: x.find_element_by_class_name('android.webkit.WebView'))
# contexts = driver.contexts
# print(contexts)
# print('switch conetext')
# driver.switch_to.context('WEBVIEW_com.wondershare.drfone')
# print('edit email')
# driver.find_element_by_id('email').send_keys('shuqing@wondershare.cn')
# print('click sendBtn')
# driver.find_element_by_class_name('btn_send').click()
#
# # 切换context 点击返回
# driver.switch_to.context('NATIVE_APP')
# driver.find_element_by_class_name('android.widget.ImageButton').click()
