# coding=utf-8
import os, sys
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi


def touch(device, x, y, t=5):
    device.touch(x, y, "md.DOWN_AND_UP")
    mr.sleep(t)


def snapshot(device, name):
    result = device.takeSnapshot()
    im_path = "C:\\zmjj\\store\\%s.png" % name
    result.writeToFile(im_path, 'png')
    mr.sleep(2)


def store(device):
    i = 0
    touch(device, 800, 40)
    snapshot(device, "gold_store")
    print "buy gold"
    for y in range(2):
        "金币购买截图"
        for x in range(3):
            touch(device, 300 + x * 230, 190 + y * 210)
            snapshot(device, i)
            touch(device, 540, 360)
            i += 1
    print "buy diamond"
    touch(device, 80, 200)
    snapshot(device, "diamond_store")
    "钻石购买截图"
    touch(device, 300, 190)
    snapshot(device, "diamond_weixin")
    touch(device, 25, 40, 3)
    touch(device, 50, 20)
    # device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
    print "Done"


if __name__ == '__main__':
    device = mr.waitForConnection(5, '127.0.0.1:21503')
    if not device:
        print >> sys.stderr, "fail"
        sys.exit(1)
    else:
        print 'connnect success'
    store(device)
