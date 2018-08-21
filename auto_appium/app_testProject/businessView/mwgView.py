import logging
from common.common_fun import Common, NoSuchElementException, TimeoutException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .loginView import LoginView


class MwgView(Common):
    searchBtn = (By.ID, '')

    def open_mwg(self):
        self.driver.findelement(*self.searchBtn).send_keys()
