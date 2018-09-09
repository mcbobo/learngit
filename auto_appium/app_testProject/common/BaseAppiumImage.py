# coding:utf-8
import os
import tempfile
import aircv as ac
import cv2
# import pytesseract
import time
from common.BaseImage import image_to_str
from selenium.common.exceptions import NoSuchElementException

TPATH = lambda p: os.path.abspath(p)
TEMP_FILE = TPATH(tempfile.gettempdir() + "/temp_screen.png")


# def set_imageSize(func):
#     def wapper(self, imobj, imsrc=None):
#         self.driver.get_screenshot_as_file(TEMP_FILE)
#         if self.get_window_size().get('height') == 500:
#             imsrc = ac.imread(TEMP_FILE)
#             return func(imobj, imsrc)
#         else:
#             img = Image.open(TEMP_FILE)
#             img.thumbnail((900, 500), Image.ANTIALIAS)
#             img.save(TEMP_FILE, 'png')
#             imsrc = ac.imread(TEMP_FILE)
#             return func(imobj, imsrc)
#
#     return wapper


class BaseView:
    def __init__(self, driver):
        self.driver = driver

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    # @set_imageSize
    @classmethod
    def find_element_by_image(self, img_path):
        # 根据路径图片得到设备上的坐标,resolution为设备的分辨率字典比例（分辨率默认为900x500）
        resolution = {1920: 2.13, 1280: 1.42, 1812: 2.013, 900: 1}
        flag = 0
        # width = self.get_window_size().get('width')
        width, height = [self.get_window_size()[k] for k in ('width', 'height')]
        while flag < 3:
            imobj = ac.imread(img_path)
            self.driver.get_screenshot_as_file(TEMP_FILE)
            imsrc = ac.imread(TEMP_FILE)
            if width != 900 and width > height:
                imsrc = cv2.resize(imsrc, (900, 500))
            else:
                imsrc = cv2.resize(imsrc, (500, 900))
            try:
                pos = ac.find_template(imsrc, imobj, 0.7).get('result')
            except AttributeError:
                flag += 1
                time.sleep(3)
            else:
                return [tuple([i * resolution[width] for i in pos])]
        raise NoSuchElementException('can not find element')

    def _room_id_image(self):
        # 自定义截取范围，得到一个大概的房间id位置的图片（智萌德州房间id，写死了截取范围）
        self.driver.get_screenshot_as_file(TEMP_FILE)
        image = cv2.imread(TEMP_FILE)
        # p = r'D:\room.png'
        # image = cv2.imread(p)
        # image = Image.open(p)
        # (x, y) = image.size
        # x1, x2, y1, y2 = x * 0.14, x * 0.21, y * 0.03, y * 0.09
        x, y = image.shape[:2]
        return image[int(x * 0.02):int(x * 0.08), int(y * 0.166):int(y * 0.234)]

    def room_id(self):
        # 识别图中数字并提取
        room_id_img = self._room_id_image()
        # img = image_processing(room_id_img)
        # room_num = pytesseract.image_to_string(img, lang="eng", config="-psm 7")
        # code = code.encode('utf-8')
        # num = filter(str.isdigit, code)
        # num = room_num.strip().split(' ')
        num = image_to_str(room_id_img).strip().split(' ')
        return num[0] if len(num[0]) > 2 else num[1]


if __name__ == '__main__':
    from common.desired_caps import appium_desired

    star_time = time.time()
    # path = r'../picture/loginBtn.png'
    # path = r'D:\room1.png'
    driver = appium_desired()
    print(BaseView(driver).room_id())
    end_time = time.time()
    print('total time:%s' % (end_time - star_time))
