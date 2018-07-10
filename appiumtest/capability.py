from  appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps = {}
desired_caps['deviceName'] = 'HMKNW17A14019270'
desired_caps['platformName'] = 'Android'
desired_caps['browserName'] = ''
desired_caps['platforVersion'] = '7.0.0'
desired_caps['automationName'] = 'uiautomator2'
desired_caps['appPackage']='com.tal.kaoyan'
desired_caps['appActivity']='com.tal.kaoyan.ui.activity.SplashActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.implicitly_wait(5)


def check_cancelBtn():
    print('check cancelBtn')

    try:
        cancelBtn = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        print('no cancelBtn')
    else:
        cancelBtn.click()


def check_skipBtn():
    print('check skipBtn')

    try:
        skipBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        print('no skipBtn')
    else:
        skipBtn.click()


check_cancelBtn()
# check_skipBtn()
