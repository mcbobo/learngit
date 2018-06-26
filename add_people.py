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
            break
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
    touch(device, 600, 400)
    touch(device, 800, 50)
    print "friend's battle"
    touch(device, 760, 400)
    print "type number"
    touch(device, 740, 250, 2)
    type_number(room_name)
    print "comfirm"
    touch(device, 330, 420, 3)
    touch(device, 520, 440, 3)
    print "exit"
    touch(device, 40, 25)
    touch(device, 100, 45, 2)
    touch(device, 350, 380, 2)
    touch(device, 40, 25)
    print "zhujiemian"
    touch(device, 785, 467, 2)
    touch(device, 690, 160, 2)


def type_number(room_name):
    numlist = {}
    num = 0
    room_name = str(room_name)

    for i in open("D:\\numlist.txt"):
        numlist[num] = i.strip()
        num += 1

    for i in room_name:
        numlist[int(i)]


def threadingGo(dev, room_name):
    threads = []
    len_dev = len(dev)
    for i in range(len_dev):
        name = '%s%s' % ('t', i)
        name = threading.Thread(target=run, args=(dev[i], room_name))
        threads.append(name)
    return threads


def add_people(runtime, room_name):
    devices_xx = connect()
    i = 0
    while i < runtime:
        threads = threadingGo(devices_xx, room_name)
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        i += 1


if __name__ == '__main__':
    add_people(4, 202977)
