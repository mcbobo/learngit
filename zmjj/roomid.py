# coding:utf-8
from PIL import Image
import pytesseract


def pic_to_num(pic_ptah):
    "识别图中数字并提取"
    image = Image.open(pic_ptah)
    code = pytesseract.image_to_string(image)
    code = code.encode('utf-8')
    num = filter(str.isdigit, code)
    return num