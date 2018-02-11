# coding:utf-8
import os


def rename(dir_path, name):
    num = 0
    for file in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, file)):
            if file.find('.png'):
                newname = '%s%s.png' % (name, num)
                os.rename(os.path.join(dir_path, file), os.path.join(dir_path, newname))
                num += 1
                print file, 'ok'


def browse_folder(srcdir):
    '遍历文件夹下所有文件夹，包括子文件夹'
    alldir = []
    for src, dirs, filenames in os.walk(srcdir):
        for dir in dirs:
            fname = os.path.abspath(dir)
            alldir.append(fname)
    return alldir


# if __name__ == '__main__':
#     while True:
#         print '''选择：
#         1.一个文件夹下多个文件夹批量改名
#         2.单个文件夹批量改名
#         3.退出
#         '''
#         ch = input('您想要的是：')
#         path = raw_input('请输入修改的文件夹：')
#         if ch == 1:
#             for dir in os.listdir(path):
#                 dir_path = os.path.abspath(dir)
#                 print dir_path
#                 rename(dir_path, dir)
#             print "DONE！"
#         elif ch == 2:
#             name = path.split('\\')
#             rename(path, name)
#             print "DONE！"
#         else:
#             break
path = raw_input('请输入修改的文件夹：')
name = path.split('\\')[-1]
print name
rename(path, name)
# ll = browse_folder(r'D:\img\test')
