# coding:utf-8
import os


def udid():
    """返回已连接设备的udid"""
    device_list = []

    cmd = 'adb devices'
    devices = os.popen(cmd).readlines()
    len_devices = len(devices) - 1
    for i in range(1, len_devices):
        device_list.append(devices[i].split('\t')[0])
    return device_list


if __name__ == '__main__':
    print(udid())
