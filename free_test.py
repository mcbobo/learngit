import cv2
import datetime

# import numpy as np
#
# img_path = 'D:\\room_test.jpg'
# img_path2 = 'D:\\room_test2.jpg'
# img2 = cv2.imread(img_path)
# img3 = cv2.imread(img_path2)
# img_pp = []
# img_pp.append(img2)
# img_pp.append(img3)
# b = np.array(img_pp)
# cv2.imwrite("D:\\img_pp.jpg", b)
# cv2.namedWindow("Image")
# cv2.imshow("Image", img_pp)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
path = r'D:\log.txt'
# img = cv2.imread(path, cv2.CV_LOAD_IMAGE_UNCHANGED)
# img = img[:, 10:25]
# cv2.namedWindow("Image")
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # cv2.imwrite(path, img)
srcstr1 = 'abc'
dststr1 = 'mno'
string1 = 'Abcdef'
srcstr2 = 'abcDef'
dststr2 = 'mno'
string2 = 'Abcdefghi'


def tr(srcstr, dststr, string, case=0):
    mylist = []
    if 0 == case:
        dicta = dict(zip(srcstr.lower(), dststr))
        if len(srcstr) > len(dststr):
            dicta.update({}.fromkeys(srcstr[len(dststr):]))
        for ch in string.lower():
            if ch in dicta:
                mylist.append(dicta[ch])
            else:
                mylist.append(ch)
    else:
        dicta = dict(zip(srcstr, dststr))
        if len(srcstr) > len(dststr):
            dicta.update({}.fromkeys(srcstr[len(dststr):]))
        for ch in string:
            if ch in dicta:
                mylist.append(dicta[ch])
            else:
                mylist.append(ch)
    print mylist
    mylist = [ch for ch in mylist if ch]
    print mylist
    print ''.join(mylist)


tr(srcstr1, dststr1, string1, 0)
tr(srcstr2, dststr2, string2, 1)