# coding:utf-8
from base import Appium_Extend


class Action():
    def __init__(self, driver):
        self.driver = driver
        self.base = Appium_Extend(self.driver)

    def touch(self, action_name):
        '输入路径中图片的名字点击模拟器对应的位置'
        impath = r'D:\appium_test\zmjj\Action\%s.png' % action_name
        self.base.get_element(impath)

    def room_id(self):
        image_box = self.base.get_screenshot_of_room_id()
        image = self.base.image_resize(image_box,2)
        num = self.base.get_image_number(image)
        return num

