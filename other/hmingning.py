import urllib.request
import random
import string
import os


def getFileNum(path):
    fileNum = 0
    for lists in os.listdir(path):
        sub_path = os.path.join(path, lists)
        if os.path.isfile(sub_path):
            fileNum += 1
    return fileNum


fileNum = getFileNum('D:\\img\\laji');


def getImg():
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(28):
        sa.append(random.choice(seed))
    salt = ''.join(sa)

    page = urllib.request.urlopen("http://cover.acfunwiki.org/cover.php")
    html = page.read()
    header = page.info()
    type = header['Content-type']

    if type == 'image/jpeg':
        name = salt + '.jpg'
    elif type == 'images/gif':
        name = salt + '.gif'

    saveFile = open('./pic/' + name, 'wb+')
    saveFile.write(html)
    saveFile.close()


count = fileNum;
while count <= 5:
    getImg()
    count += 1
    num = str(count)
    print('成功抓取第' + num + "张图片")
