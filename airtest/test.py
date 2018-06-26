# -*-coding:utf-8-*-
from airtest.core.api import *

# connect an android phone with adb
connect_device("Android:///127.0.0.1:21543")
# install(r'D:\img\AE86\zmpt_test.apk')
start_app('com.zhimengsports.zmpt')
v = r'D:/test.png'
touch(v)
