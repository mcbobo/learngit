from baseView.baseView import BaseView
from selenium.common.exceptions import NoSuchElementException
from common.desired_caps import appium_desired
import logging
import time
import os
import csv
import yaml


class Common(BaseView):
    loginBtn = r"../picture/loginBtn.png"
    sign_inBtn = r"../picture/sign_inBtn.png"
    updateBtn = r""

    def check_loginBtn(self):
        logging.info('==========check_loginBtn=========')

        try:
            button = self.find_element(self.loginBtn)
        except NoSuchElementException:
            logging.info('no loginBtn')
        else:
            self.driver.tap(button)

    def check_sign_inBtn(self):
        logging.info('=========check sign_inBtn=============')

        try:
            button = self.find_element(self.sign_inBtn)
        except NoSuchElementException:
            logging.info('no sign_inBtn')
        else:
            self.driver.tap(button)

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
        y1 = int(l[1] * 0.75)
        y2 = int(l[1] * 0.25)
        self.swipe(x1, y1, x1, y2)

    def swipeUp(self):
        logging.info('swipeUp')
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.75)
        self.swipe(x1, y1, x1, y2)

    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self, module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, time)

        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)

    def check_updateBtn(self):
        logging.info('====check_update====')
        try:
            element = self.find_element(self.updateBtn)
        except NoSuchElementException:
            pass
        else:
            logging.info('update version')
            self.driver.tap(element)

    def get_csv_data(self, csv_file, line):
        logging.info('=====get_csv_data======')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

    def tap_room_id(self, num):
        with open('../config/room_num.yaml', 'r', encoding='utf-8') as file:
            room_id = yaml.load(file)
        base_dir = os.path.dirname(os.path.dirname(__file__))
        room_id_path = os.path.join(base_dir, 'picture', 'number', room_id[num])
        self.find_element(room_id_path)


if __name__ == '__main__':
    # driver = appium_desired()
    # com = Common(driver)
    # com.check_loginBtn()
    # com.check_sign_inBtn()
    # com.swipeLeft()
    # com.getScreenShot('startApp')
    # com.tap_room_id(9)

    list = ["这", "是", "一/个", "测试", "数据"]
    # for i in range(len(list)):
    # print(i, list[i])

    list1 = ["这", "是", "一个", "测试", "数据"]
    # for index, item in enumerate(list1):
    #     print(index, item)
