# coding:utf-8
import sys, time, threading
from random import randint
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md


def connect():
    templist = []
    deviceslist = []
    devices = []

    f = open("D:\\devices.txt")
    while True:
        line = f.readline()
        if line:
            templist.append(line.strip())
        else:
            break;
    f.close()
    templist.pop(0)
    len_templist = len(templist) - 1
    for i in range(0, len_templist):
        deviceslist.append(templist[i].split('\t'))

    for i in range(len(deviceslist)):
        devices.append(mr.waitForConnection(1.0, deviceslist[i][0]))
        if not devices:
            print >> sys.stderr, "fail"
            sys.exit(1)
        else:
            print 'connnect success'
    return devices


def ComparePic(device):
    pic = device.takeSnapshot()
    newpic = device.takeSnapshot()
    return pic.sameAs(newpic, 0.9)


def touch(device):
    x = randint(10, 880)
    y = randint(10, 490)
    device.touch(x, y, 'DOWN_AND_UP')


def other(device, same):
    # same = ComparePic(device)
    if same:
        device.press('KEYCODE_BACK', 'DOWN_AND_UP')
        mr.sleep(2)


def run(device, i=0):
    # i = 0
    pic = device.takeSnapshot()
    while i < 20:
        touch(device)
        i += 1
    newpic = device.takeSnapshot()
    same = pic.sameAs(newpic, 0.9)
    other(device, same)


def threadingGo(dev):
    threads = []
    len_dev = len(dev)
    for i in range(len_dev):
        name = '%s%s' % ('t', i)
        name = threading.Thread(target=run, args=(dev[i], 0))
        threads.append(name)
    return threads


if __name__ == '__main__':
    devices_xx = connect()
    # path = 'D:\\appium_test\\zmjj\\screen_shot\\lala.png'
    # result = mr.loadImageFromFile(path)
    while True:
        threads = threadingGo(devices_xx)
        for t in threads:
            t.start()
        for t in threads:
            t.join()
