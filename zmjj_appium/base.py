# coding:utf-8
import os
import time
import tempfile
import aircv as ac
import pytesseract
from PIL import Image

PATH = lambda p: os.path.abspath(p)
TEMP_FILE = PATH(tempfile.gettempdir() + "/temp_screen.png")


class Appium_Extend(object):
    def __init__(self, driver):
        self.driver = driver

    def get_time(self):
        tamp = int(time.time())
        return tamp

    def screen_shot(self):
        '模拟器全屏截图'
        im_name = self.get_time()
        filename = r'D:\appium_test\zmjj\%s.png' % im_name
        self.driver.get_screenshot_as_file(filename)

    def get_screenshot_by_custom_size(self, box):
        '自定义截取范围'
        self.driver.get_screenshot_as_file(TEMP_FILE)
        image = Image.open(TEMP_FILE)
        newImage = image.crop(box)
        # newImage.save(TEMP_FILE)
        return newImage

    def get_screenshot_of_roomid(self):
        '自定义截取范围，得到一个大概的房间id位置的图片'
        self.driver.get_screenshot_as_file(TEMP_FILE)
        image = Image.open(TEMP_FILE)
        (x, y) = image.size
        x1, x2, y1, y2 = x * 0.14, x * 0.21, y * 0.03, y * 0.09
        box = (x1, x2, y1, y2)
        newImage = image.crop(box)
        # newImage.save(TEMP_FILE)
        return newImage

    def get_element(self, im_path):
        '根据路径图片得到模拟器上的坐标'
        imobj = ac.imread(im_path)
        self.driver.get_screenshot_as_file(TEMP_FILE)
        imsrc = ac.imread(TEMP_FILE)
        pos = ac.find_template(imsrc, imobj, 0.7).get('result')
        return pos

    def get_roomid_position(self, im_path):
        '根据路径图片得到房间id在模拟器上的坐标'
        imobj = ac.imread(im_path)
        self.driver.get_screenshot_as_file(TEMP_FILE)
        imsrc = ac.imread(TEMP_FILE)
        pos = ac.find_template(imsrc, imobj).get('rectangle')
        return pos

    def retry(self, function):
        '传入一个有返回的操作函数，重试3次'
        for i in range(3):
            value = function
            if value:
                break
            time.sleep(2)
        return value

    def get_image_number(self, image):
        "识别图中数字并提取"
        code = pytesseract.image_to_string(image)
        code = code.encode('utf-8')
        num = filter(str.isdigit, code)
        return num

    def image_resize(self, image, image_size):
        (x, y) = image.size
        xsize = x * image_size
        ysize = y * image_size
        image = image.resize((xsize, ysize), resample=3)
        return image
