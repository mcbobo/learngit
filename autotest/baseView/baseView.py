# coding:utf-8
import os
import tempfile
import aircv as ac
import pytesseract
from PIL import Image
from time import sleep

PATH = lambda p: os.path.abspath(p)
TEMP_FILE = PATH(tempfile.gettempdir() + "/temp_screen.png")


class BaseView(object):
    def __init__(self, driver):
        self.driver = driver

    # def find_element(self, *loc):
    #     return self.driver.find_element(*loc)

    # def find_elements(self, *loc):
    #     return self.driver.find_elements(*loc)

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def find_element(self, img_path):
        '根据路径图片得到模拟器上的坐标'
        flag = 0
        while flag < 3:
            imobj = ac.imread(img_path)
            self.driver.get_screenshot_as_file(TEMP_FILE)
            imsrc = ac.imread(TEMP_FILE)
            try:
                pos = ac.find_template(imsrc, imobj, 0.7).get('result')
            except AttributeError:
                flag += 1
                sleep(3)
            else:
                break
        return pos

    def _roomid_image(self):
        '自定义截取范围，得到一个大概的房间id位置的图片'
        self.driver.get_screenshot_as_file(TEMP_FILE)
        image = Image.open(TEMP_FILE)
        (x, y) = image.size
        x1, x2, y1, y2 = x * 0.14, x * 0.21, y * 0.03, y * 0.09
        return image.crop(x1, x2, y1, y2)

    def roomid(self):
        "识别图中数字并提取"
        roomid_img = self._roomid_image()
        code = pytesseract.image_to_string(roomid_img)
        code = code.encode('utf-8')
        num = filter(str.isdigit, code)
        return num
