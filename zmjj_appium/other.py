# coding:utf-8
import cv2
from PIL import Image, ImageFilter
import pytesseract
import aircv as ac
import os
from numpy import mat
import tempfile

PATH = lambda p: os.path.abspath(p)
TEMP_FILE = PATH(tempfile.gettempdir() + "/temp_screen.png")


def get_image_number(image):
    "识别图中数字并提取"
    code = pytesseract.image_to_string(image)
    code = code.encode('utf-8')
    num = filter(str.isdigit, code)
    return num


def image_resize(image, image_size):
    (x, y) = image.size
    xsize = x * image_size
    ysize = y * image_size
    image = image.resize((xsize, ysize), resample=3)
    return image


def retry(function):
    for i in range(3):
        value = function
        if value:
            break
        print i
    return value


def binarization(image):
    # 转成灰度图
    imgry = image.convert('L')
    # 二值化，阈值可以根据情况修改
    threshold = 128
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    out = imgry.point(table, '1')
    return out


def find_element(imobj):
    imobj = ac.imread(imobj)
    imsrc = ac.imread(r'D:\room.jpg')
    pos = ac.find_template(imsrc, imobj, 0.7)
    return pos


# image_filepath = r'D:\room_id.png'
# newImage.save(image_filepath)
# img = cv2.imread(image_filepath)
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


image_path = r'D:\room.jpg'
im = Image.open(image_path)
(x, y) = im.size
box = (x * 0.15, y * 0.03, x * 0.21, y * 0.09)
newImage = im.crop(box)
im = image_resize(newImage, 2)
# im = im.filter(ImageFilter.SHARPEN)
im.save(r'D:\tes1.jpg')
num = get_image_number(im)
print num


# img = Image.open(im)
# binarization(img).save(r'D:\bb.png')
# img = cv2.imread("D:\\cat.jpg")
# img2 = cv2.imwrite(r"D:\cat2.png",img)
# cv2.namedWindow("Image")
# cv2.imshow("Image", img2)
# cv2.waitKey (0)
# cv2.destroyAllWindows()
