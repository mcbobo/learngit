# coding:utf-8
import datetime
from selenium import webdriver
import unittest
from time import sleep
import datetime
from selenium.webdriver.support.ui import Select


def str_trans_time(string):
    date_time = datetime.datetime.strptime(string, '%y-%m-%d').date()
    return date_time


def count_days(dt1, dt2):
    delta = abs(dt1 - dt2)
    return delta.days


# if __name__ == '__main__':
#     date_time1 = raw_input('请输入格式为YY-MM-DD格式的日期:')
#     date_time2 = raw_input('请输入格式为YY-MM-DD格式的日期:')
#     temp1 = str_trans_time(date_time1)
#     temp2 = str_trans_time(date_time2)
#     result = count_days(temp1, temp2)
#     print result


def test():
    for i in range(1, 3):
        print i


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get(r'http://test.gytycn.com/zmpt_system_manage/index.php/Home/Index')
    sleep(2)
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin123")
    driver.find_element_by_xpath("/html/body/div/div/form/button").click()
    driver.find_element_by_xpath("/html/body/div[2]/nav/div[2]/div[1]/ul/li[12]/a/span[1]").click()
