import os
import sys
import unittest
from common.BaseRunner import ParametrizedTestCase
from PageObject.Home.FirstOpenPage import FirstOpenPage
from common.BaseYaml import getMultiYam
from common.BaseSetupDown_new import UpDown

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


# class HomeTest(ParametrizedTestCase):
class HomeTest(UpDown):
    # @unittest.skip('testFirstOpen')
    # def testFirstOpen(self):
    #     # app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/home/firstOpen.yaml"),
    #     #        "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
    #     data = getMultiYam(PATH("../yamls/home/firstOpen.yaml"))
    #     app = {"logTest": self.logTest, "driver": self.driver, "data": data,
    #            "device": self.devicesName, "caseName": 'test_open'}
    #
    #     page = FirstOpenPage(app)
    #     page.operate()
    #     page.checkPoint()

    def testLogin(self):
        # app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/home/firstOpen.yaml"),
        #        "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
        casename = 'multi_testcase'
        t1 = r'D:\soft\pyc\test\auto_appium\app_testProject\yamls\home\firstOpen.yaml'
        t2 = r'D:\soft\pyc\test\auto_appium\app_testProject\yamls\home\login.yaml'
        self.template(casename, t1, t2)

        # def template(self, case_name, *args):
        #     data = getMultiYam(*args)
        #     app = {"logTest": self.logTest, "driver": self.driver, "data": data,
        #            "device": self.devicesName, "caseName": case_name}
        #
        #     page = FirstOpenPage(app)
        #     page.operate()
        #     page.checkPoint()
        #
        # @classmethod
        # def setUpClass(cls):
        #     super(HomeTest, cls).setUpClass()
        #
        # @classmethod
        # def tearDownClass(cls):
        #     super(HomeTest, cls).tearDownClass()
