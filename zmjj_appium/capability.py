from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:21533'
desired_caps['platforVersion'] = '4.4.4'
# desired_caps['automationName'] = 'uiautomator2'

# desired_caps['app'] = r'C:\Users\Shuqing\Desktop\kaoyan3.1.0.apk'
desired_caps['appPackage'] = 'com.zhimengsports.zmpt'
desired_caps['appActivity'] = 'org.cocos2dx.javascript.AppActivity'

desired_caps['noReset'] = 'False'
desired_caps['unicodeKeyboard'] = "True"
desired_caps['resetKeyboard'] = "True"

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(2)

