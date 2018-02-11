# coding:utf-8


def connect():
    "连接D盘devices.txt中的设备"
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


def snapshot(device, name):
    result = device.takeSnapshot()
    im_path = "C:\\zmjj\\store" + str(name) + ".png"
    result.writeToFile(im_path, 'png')
    mr.sleep(2)
