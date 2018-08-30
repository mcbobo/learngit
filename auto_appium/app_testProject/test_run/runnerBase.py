__author__ = 'shikun'
# -*- coding: utf-8 -*-
import unittest
from appium import webdriver
# from common.variable import GetVariable as common
import os
from selenium import webdriver as web
# from seleniumrequests import Chrome
# from testBLL import apkBase
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging
import logging.config

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def appium_testcase(l_devices):
    desired_caps = {}
    desired_caps['platformName'] = l_devices["platformName"]
    desired_caps['platformVersion'] = l_devices["platformVersion"]
    desired_caps['deviceName'] = l_devices["deviceName"]
    desired_caps['appPackage'] = l_devices["appPackage"]
    desired_caps['appActivity'] = l_devices["appActivity"]
    desired_caps['udid'] = l_devices["deviceName"]
    desired_caps['app'] = l_devices["app"]
    desired_caps["unicodeKeyboard"] = "True"
    desired_caps["resetKeyboard"] = "True"
    logging.info('appium port:%s start run %s' % (l_devices["port"], l_devices["udid"]))
    logging.info('start app...')
    remote = "http://127.0.0.1:" + str(l_devices["port"]) + "/wd/hub"
    driver = webdriver.Remote(remote, desired_caps)
    return driver


class TestInterfaceCase(unittest.TestCase):
    def __init__(self, methodName='runTest', l_devices=None):
        super(TestInterfaceCase, self).__init__(methodName)
        self.l_devices = l_devices
        # self.driver = ""

    @staticmethod
    def setUpClass():
        # global driver
        # ga = get_evices()
        # common.SELENIUM_APPIUM = ga.selenium_appium
        # if common.SELENIUM_APPIUM == common.APPIUM: # appium入口
        #     if ga.platformName == common.ANDROID and common.FLAG:
        #         appium_testcase(ga)
        # if common.SELENIUM_APPIUM == common.SELENIUM and common.FLAG: # selenium入口
        #     selenium_testcase(ga)
        #     # driver.get("http://www.baidu.com")
        #     # data = driver.title
        pass

    def setUp(self):
        self.driver = appium_testcase(self.l_devices)

    def tearDown(self):
        # self.driver.close_app()
        # self.driver.quit()
        pass

    @staticmethod
    def tearDownClass():
        # driver.close_app()
        # driver.quit()
        print('tearDownClass')

    @staticmethod
    def parametrize(testcase_klass, l_devices=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, l_devices=l_devices[0]))
        return suite


if __name__ == '__main__':
    from devices import devices
    from test_case.test_login import TestLogin

    suite = unittest.TestSuite()
    suite.addTest(TestInterfaceCase.parametrize(TestLogin, devices()[0]))
    unittest.TextTestRunner(verbosity=2).run(suite)
