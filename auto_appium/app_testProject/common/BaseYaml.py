# -*- coding:utf-8 -*-
import yaml


def getYam(path='../config/app_caps.yaml'):
    try:
        with open(path, encoding='utf-8') as f:
            x = yaml.load(f)
            return x
    except FileNotFoundError:
        print(u"找不到文件")
