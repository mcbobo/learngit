# -*- coding: utf-8 -*-
import sys

sys.path.append("..")
import datetime
import time
import unittest
import os
from multiprocessing import Pool
from multiprocessing import Process
import subprocess
from runnerBase import TestInterfaceCase
from appiuim_service.devices import devices
import logging
from test_case.test_login import TestLogin

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def get_devices():
    return devices()


ga = get_devices()


def runnerPool():
    # devices_Pool = []
    devices_Pool = ga
    # for i in range(0, len(ga["appium"])):
    #     l_pool = []
    #     t = {}
    #     t["deviceName"] = ga["appium"][i]["devices"]
    #     t["platformVersion"] = phoneBase.get_phone_info(devices=ga["appium"][i]["devices"])["release"]
    #     t["platformName"] = ga["appium"][i]["platformName"]
    #     t["port"] = ga["appium"][i]["port"]
    #     l_pool.append(t)
    #     devices_Pool.append(l_pool)
    pool = Pool(len(devices_Pool))
    # for i in range(2):
    #     pool.apply_async(sample_request, args=(t[i],)) # 异步
    pool.map(runnerCaseApp, devices_Pool)
    pool.close()
    pool.join()


def runnerCaseApp(l_devices):
    # start_test_time = dataToString.getStrTime(time.localtime(), "%Y-%m-%d %H:%M %p")
    starttime = datetime.datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(TestInterfaceCase.parametrize(TestLogin, l_devices=l_devices))
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.datetime.now()
    logging.info('spend %s second'%(endtime-starttime))
    # report()


if __name__ == '__main__':
    ga = get_devices()
    # print(ga)
    runnerPool()


