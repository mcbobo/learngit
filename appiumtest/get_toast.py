# coding=utf-8
from appium import webdriver
import yaml
from time import sleep
import logging

file = open('desired_caps.yaml', 'r')
data = yaml.load(file)

logging.basicConfig(filename=r'D:\runlog.log', level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

desired_caps = {}
desired_caps['platformName'] = data['platformName']
desired_caps['platformVersion'] = data['platformVersion']
desired_caps['deviceName'] = data['deviceName']

desired_caps['app'] = data['app']
desired_caps['noReset'] = data['noReset']

desired_caps['appPackage'] = data['appPackage']
desired_caps['appActivity'] = data['appActivity']

logging.info('start app..')
driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)

logging.info('Done!')
sleep(3)
driver.close_app()
