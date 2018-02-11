# coding:utf-8
import cv2
import numpy as np

print 'loading  ...'


def showpiclocation(img, findimg):  # 定义定位函数
    # 定位图片
    w = img.shape[1]  # 返回img的第二维度长度---宽度
    h = img.shape[0]  # 返回img的第一维度长度---高度
    fw = findimg.shape[1]
    fh = findimg.shape[0]
    findpt = None
    for now_h in xrange(0, h - fh):
        for now_w in xrange(0, w - fw):
            comp_tz = img[now_h:now_h + fh, now_w:now_w + fw, :] - findimg
            if np.sum(comp_tz) < 1:
                findpt = now_w, now_h
        # print ".",
    if findpt != None:
        cv2.rectangle(img, findpt, (findpt[0] + fw, findpt[1] + fh), (0, 0, 255))  # opencv函数画矩形
    return img


fn = r'D:\room.jpg'
fn2 = r'D:\button.jpg'
myimg = cv2.imread(fn)
myimg2 = cv2.imread(fn2)
myimg = showpiclocation(myimg, myimg2)
cv2.namedWindow('img')
cv2.imshow('img', myimg)
cv2.waitKey()
cv2.destroyAllWindows()
