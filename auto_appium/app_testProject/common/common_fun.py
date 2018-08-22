from baseView.baseView import BaseView
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging
from selenium.webdriver.common.by import By
import time
import os
import csv
import subprocess


class Common(BaseView):
    def fast_input(str, element):
        '快速输入'
        x = subprocess.check_output('adb devices', shell=True).split('\n')[1][:-7]
        element.click()
        time.sleep(0.3)
        subprocess.Popen('adb -s %s shell input text %s' % (x, str), shell=True)
        time.sleep(0.5)

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipeLeft(self):
        logging.info('swipeLeft')
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.swipe(x1, y1, x2, y1, 1000)

    def swipeDown(self):
        logging.info('swipeDown')
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.1)
        y2 = int(l[0] * 0.9)
        self.swipe(x1, y1, x1, y2, 1000)

    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self, module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, time)

        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)

    def get_csv_data(self, csv_file, line):
        logging.info('=====get_csv_data======')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row


if __name__ == '__main__':
    driver = appium_desired()
    com = Common(driver)
    time.sleep(5)
    com.swipeLeft()
    com.getScreenShot('startApp')
