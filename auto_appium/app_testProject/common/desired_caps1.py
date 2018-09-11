from appium import webdriver
import yaml
import logging
import logging.config
import os

CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def appium_desired():
    with open('../config/app_caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']

    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_dir, 'app', data['appname'])
    desired_caps['app'] = app_path

    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']

    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    # toast location setting
    # desired_caps['automationName'] = 'uiautomator2'

    logging.info('start app...')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(8)
    return driver


if __name__ == '__main__':
    import sys


    filenames = os.listdir(fdirp)

    class T1:
        @staticmethod
        def app():
            app = {'other': 'lala'}
            return app

        def test1(self):
            t1 = self.app()
            t1["caseName"] = sys._getframe().f_code.co_name
            return t1

        def test2(self):
            t2 = T1.app()
            t2["caseName"] = sys._getframe().f_code.co_name
            return t2


    t = T1()
    print(t.test1())
    print(t.test2())
    print(t.app())
