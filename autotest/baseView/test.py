from PIL import Image
import cv2
import numpy as np
import pytesseract


def get_bin_table(threshold=230):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table


p = r'D:\room.png'
image = cv2.imread(p)
b, g, r = cv2.split(image)
cv2.imshow("Blue", r)
cv2.imshow("Red", g)
cv2.imshow("Green", b)
cv2.waitKey(0)
cv2.destroyAllWindows()
