# -*-coding:utf-8-*-
from airtest.core.api import *
import tempfile
import aircv as ac

PATH = lambda p: os.path.abspath(p)
TEMP_FILE = PATH(tempfile.gettempdir() + "/temp_screen.png")


def get_element(imobj_path, imsrc_path):
    '根据路径图片得到模拟器上的坐标'
    imobj = ac.imread(imobj_path)
    imsrc = ac.imread(imsrc_path)
    pos = ac.find_template(imsrc, imobj, 0.9).get('result')
    return pos


# connect an android phone with adb
connect_device("Android:///HMKNW17A14019270")
# # install(r'D:\img\AE86\zmpt_test.apk')
start_app('com.zhimengsports.zmpt')
sleep(3)
login_path = r"D:\test.jpg"
img_path = snapshot(filename=r"D:\sreen.jpg")
# button_pos = get_element(img_path, img_path)
# print button_pos
# touch(button_pos)
