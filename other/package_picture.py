# coding:utf-8
import os
import json
import math
from PIL import Image

'''多图合并'''

tf = []
sizetmp = []
fullnames = []
fdir = []


def opd(rootdir):
    for rt, dirs, filenames in os.walk(rootdir):
        for dirname in dirs:
            fname = os.path.join(rootdir, dirname)
            fdir.append(fname)


def opf(fdirp):
    'open dir all png file except name with out'
    # global num
    num = 0
    filenames = os.listdir(fdirp)
    for filename in filenames:
        fullname = os.path.join(fdirp, filename)
        if fullname[-7:-4] == r"out" or fullname[-4:] != r".png":
            continue
        fullnames.append(fullname)
        num += 1
    return num


def ftoi(bili):
    '通过路径打开图像文件，设置文件的大小'
    for i in range(len(fullnames)):
        image = fullnames.pop(0)
        imtmp = Image.open(image)
        '设置长(x)和宽(y)'
        x_size = int(bili * imtmp.size[0])
        y_size = int(bili * imtmp.size[1])
        im = imtmp.resize((x_size, y_size))
        '裁剪图片'
        box = (2, 0, x_size - 2, y_size)
        im = imtmp.crop(box)
        sizetmp.append(im.size)
        tf.append(im)


def smarts(num):
    '确定合并的长和宽'
    n1, n2, i, l = 0, 0, 0, 0
    y = int(math.sqrt(num))
    if num == 2:
        return 1, 2
    elif num == 1:
        return 1, 1
    else:
        if y * y == num:
            return y, y
        else:
            while n1 < num:
                n1 = y * (y + i)
                i += 1
            while n2 < num:
                n2 = (y - 1) * (y + l)
                l += 1
            if (n2 - num) > (n1 - num) or n2 == n1:
                return y, y + (i - 1)
            else:
                return y - 1, y + (l - 1)


def c_dic(fdirp, new_dic):
    'json文件'
    # im_info = sorted(new_dic.items(), key=lambda d: d[0])
    fp = fdirp + r'\test.json'
    with open(fp, 'w') as f_obj:
        json.dump(new_dic, f_obj)


def baseimg_size(x, y, img_size):
    base_xsize = 0
    for i in range(x):
        (xsize, ysize) = img_size[i]
        base_xsize += xsize
    base_ysize = ysize * y
    return base_xsize, base_ysize


def wrf(fdirp, ys, xs, bili):
    new_dic = {}
    ftoi(bili)
    '旧的基础图大小'
    # (x_size, y_size) = sizetmp[0]
    i = 0
    '新的拼合图的总大小'
    base_imgsize = baseimg_size(xs, ys, sizetmp)
    base_img = Image.new('RGBA', base_imgsize)
    '这个是写死的，图大小用上面的'
    # base_img = Image.new('RGBA', (xs * x_size, ys * y_size))
    for y in range(ys):
        '新的操作'
        sumxsize = 0
        for x in range(xs):
            try:
                # x_size = sizetmp[0][0]
                # y_size = sizetmp[0][1]
                '新的基础图大小'
                (x_size, y_size) = sizetmp.pop(0)
                '新的box算法'
                box_xsize0 = sumxsize
                box_xsize1 = sumxsize = sumxsize + x_size
                box_ysize0 = y * y_size
                box_ysize1 = (y + 1) * y_size
                box = (box_xsize0, box_ysize0, box_xsize1, box_ysize1)
                # box = (x * x_size, y * y_size, (x + 1) * x_size, (y + 1) * y_size)
                base_img.paste(tf.pop(0), box)
                lc = box_xsize0, box_ysize0
                '旧的，sizetmp改一下，直接用新的基础图大小'
                new_dic[i] = {'size': (x_size, y_size), 'location': lc}
                # new_dic[i] = {'size': sizetmp.pop(0), 'location': lc}
            except IndexError, e:
                print e
            i += 1
    '大图新名字'
    img_name = fdirp.split('\\')
    base_img.save(fdirp + r'\%s.png' % img_name[-1])
    '大图旧名字'
    # base_img.save(fdirp + r'\out.png')
    c_dic(fdirp, new_dic)


def dirsm():
    path = raw_input('请输入您要合并的路径：')
    bili = float(raw_input('请输入合并图片的比例：'))
    opd(path)
    for i in fdir:
        num = opf(i)
        x, y = smarts(num)
        wrf(i, x, y, bili)


def filesm():
    path = raw_input('请输入您要合并的路径：')
    bili = float(raw_input('请输入合并图片的比例：'))
    num = opf(path)
    x, y = smarts(num)
    wrf(path, x, y, bili)


if __name__ == '__main__':
    while True:
        print '''功能选择：
            1.多个文件夹图片合并
            2.单个文件夹图片合并
            3.退出
            '''
        ch = input('您想要的是：')
        if ch == 1:
            dirsm()
            print "DONE！"
        elif ch == 2:
            try:
                filesm()
            except IndexError:
                print "请输入正确的路径："
                filesm()
            print "DONE！"
        else:
            break
