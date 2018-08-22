# coding:utf-8
from baseView.baseView import BaseView
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging
from selenium.webdriver.common.by import By
import time
import os
import csv
import subprocess
import yaml


class Common(BaseView):
    def fast_input(self, str, element):
        # 快速输入
        with open('../config/app_caps.yaml', 'r', encoding='utf-8') as file:
            data = yaml.load(file)

        # x = subprocess.check_output('adb devices', shell=True).decode('utf-8').split('\n')[1][:-7]
        x = data['deviceName']
        element.click()
        time.sleep(0.3)
        subprocess.Popen('adb -s %s shell input text %s' % (x, str), shell=True)
        time.sleep(0.5)

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipe_action(self, act):
        logging.info('swipe_' + act)
        act = act.lower()
        action = {'left': [0.8, 0.2, 0.5, 0.5], 'right': [0.2, 0.8, 0.5, 0.5],
                  'up': [0.5, 0.5, 0.8, 0.2], 'down': [0.5, 0.5, 0.2, 0.8]}
        l = self.get_size()
        x1 = int(l[0] * action[act][0])
        x2 = int(l[0] * action[act][1])
        y1 = int(l[1] * action[act][2])
        y2 = int(l[1] * action[act][3])
        self.swipe(x1, y1, x2, y2, 1000)

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
    com.swipe_action('up')
    time.sleep(2)
    com.swipe_action('down')
    com.swipe_action('left')
    time.sleep(2)
    com.swipe_action('right')
    time.sleep(2)
    # com.getScreenShot('startApp')
