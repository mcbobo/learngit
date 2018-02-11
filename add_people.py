# coding:utf-8
import sys, time, threading
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


def touch(device, x, y, t=5):
    device.touch(x, y, "md.DOWN_AND_UP")
    mr.sleep(t)


def run(device, room_name):
    touch(device, 700, 350)
    touch(device, 800, 55)
    touch(device, 370, 470)
    touch(device, 460, 40, 2)
    device.type(str(room_name))
    touch(device, 650, 40)
    touch(device, 850, 150)
    touch(device, 50, 50)
    touch(device, 870, 45.2)
    touch(device, 510, 390.2)


def threadingGo(dev, room_name):
    threads = []
    len_dev = len(dev)
    for i in range(len_dev):
        name = '%s%s' % ('t', i)
        name = threading.Thread(target=run, args=(dev[i], room_name))
        threads.append(name)
    return threads

if __name__ == '__main__':
    devices_xx = connect()
    i = 0
    while i < 10:
        threads = threadingGo(devices_xx, 1144)
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        i += 1
