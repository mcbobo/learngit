from common.BaseRunner import ParametrizedTestCase
import os
import sys
from PageObject.Home.FirstOpenPage import FirstOpenPage

from businessView.loginView import LoginView
from common.BaseFile import get_csv_data

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class HomeTest(ParametrizedTestCase):
    def testFirstOpen(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/home/firstOpen.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        page = FirstOpenPage(app)
        page.operate()
        page.checkPoint()

    # def test_login_error(self):
    #     csv_file = '../data/account.csv'
    #     print('======test_login_error=====')
    #     l = LoginView(self.driver)
    #     data = get_csv_data(3, csv_file=csv_file)
    #
    #     login_fail = l.login_action(data[0], data[1], self.devicesName)
    #     self.assertFalse(login_fail, msg='login fail!')


    @classmethod
    def setUpClass(cls):
        super(HomeTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(HomeTest, cls).tearDownClass()
