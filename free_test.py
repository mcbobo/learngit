import os, json, math
import os.path
from PIL import Image

tf = []
sb = 0
'dic need array'
nametmp = []
sizetmp = []
ltmp = []
fullnames =[]


def opf(rootdir):
    'open dir all png file except name with out'
    # for parent, dirnames, filenames in os.walk(rootdir):
    global sb
    i = 0
    filenames = os.listdir(rootdir)
    for filename in filenames:
        fullname = os.path.join(rootdir, filename)
        if fullname[-7:-4] == r"out" or fullname[-4:] != r".png":
            continue
        fullnames.append(fullname)
        name = filename.split('.')
        nametmp.append(name[0])
        sb += 1


def ftoi(x_size=200, y_size=200):
    'make picture file transform image file'
    for i in fullnames:
        tmp = Image.open(i)
        im = tmp.resize((x_size, y_size))
        sizetmp.append(tmp.size)
        tf.append(im)


def smarts():
    'input file path sum file number,select what best rank'
    n1, n2, i, l = 0, 0, 0, 0
    y = int(math.sqrt(sb))
    if n1 == sb:
        return y, y
    else:
        while n1 < sb:
            n1 = y * (y + i)
            i += 1
        while n2 < sb:
            n2 = (y - 1) * (y + l)
            l += 1
        if (n2 - sb) > (n1 - sb) or n2 == n1:
            return y, y + (i - 1)
        else:
            return y - 1, y + (l - 1)


def wrf(rootdir, ys, xs, y_size=200, x_size=200):
    'ys xs set high width,x_size and y_size set picture size'
    ftoi(y_size, x_size)
    i = 0
    base_img = Image.new('RGB', (xs * x_size, ys * y_size))
    for y in range(ys):
        for x in range(xs):
            box = (x * x_size, y * y_size, (x + 1) * x_size, (y + 1) * y_size)
            try:
                base_img.paste(tf[i], box)
                ltmp.append((x * x_size, y * y_size))
            except IndexError as e:
                print e
            i += 1
    base_img.save(rootdir + r'\out.png')


def c_dic(rootdir):
    'write file to json file'
    im_info = {}
    for i in range(len(ltmp)):
        if i < 10:
            nametmp[i] = '0000' + str(i)
        else:
            nametmp[i] = '000' + str(i)
        im_info[nametmp[i]] = ltmp[i], sizetmp[i]
    im_info = sorted(im_info.items(), key=lambda d: d[0])
    fp = rootdir + r'\maliya.json'
    with open(fp, 'w') as f_obj:
        json.dump(im_info, f_obj)


path = r'D:\img\cartoon\youling'
opf(path)
# test = smarts()
# # file path,y,x,y lenght(default 200),x width(default 200)
wrf(path, 10,10,100,100 )
c_dic(path)
