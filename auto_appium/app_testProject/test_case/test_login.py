from common.myunit import StartEnd
from common.function import get_csv_data
from businessView.loginView import LoginView
import unittest
import logging


class TestLogin(StartEnd):
    csv_file = '../data/account.csv'

    @unittest.skip('test_login_135')
    def test_login_135(self):
        logging.info('======test_login_135=====')
        l = LoginView(self.driver)
        data = get_csv_data(2, csv_file=self.csv_file)

        l.login_action(data[0], data[1])
        self.assertTrue(l.check_loginStatus())

    @unittest.expectedFailure
    def test_login_137(self):
        logging.info('======test_login_137=====')
        l = LoginView(self.driver)
        data = get_csv_data(1, csv_file=self.csv_file)

        l.login_action(data[0], data[1])
        self.assertTrue(l.check_loginStatus())

    # @unittest.skip('test_login_error')
    def test_login_error(self):
        logging.info('======test_login_error=====')
        l = LoginView(self.driver)
        data = get_csv_data(3)

        login_fail = l.login_action(data[0], data[1])
        self.assertFalse(login_fail, msg='login fail!')


if __name__ == '__main__':
    unittest.main()
