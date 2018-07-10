# coding:utf-8
import os


def file_rename(dir_path, new_filename):
    num = 0
    for file in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, file)):
            if file.rfind('.'):
                file_type = file[file.rfind('.'):]
                newname = '%s%s%s' % (new_filename, num, file_type)
                try:
                    os.rename(os.path.join(dir_path, file), os.path.join(dir_path, newname))
                except WindowsError, e:
                    print e
                num += 1
                print file, 'ok'


def dir_rename(dir_path):
    dirlist = []
    for dir in os.listdir(dir_path):
        if os.path.isdir(os.path.join(dir_path, dir)):
            dirlist.append(dir)
    print dirlist
    choice_dirs = raw_input("输入需要更改文件夹的名字：")
    choice_dirlist = choice_dirs.split(',')
    for cdir in choice_dirlist:
        if cdir in dirlist:
            newname = raw_input("输入\"%s\"新的名字：" % (cdir))
            os.rename(os.path.join(dir_path, cdir), os.path.join(dir_path, newname))
            print cdir, 'ok'
        else:
            print "在%s没有%s这个文件夹" % (dir_path, cdir)


def browse_folder(srcdir):
    '遍历文件夹下所有文件夹，包括子文件夹'
    alldir = []
    for dirs in os.listdir(srcdir):
        if os.path.isdir(os.path.join(srcdir, dirs)):
            dirsname = os.path.join(srcdir, dirs)
            alldir.append(dirsname)
        for dir in os.listdir(dirsname):
            if os.path.isdir(os.path.join(dirsname, dir)):
                dirname = os.path.join(dirsname, dir)
                alldir.append(dirname)
    return alldir


def alldir_rename(srcdir):
    '批量修改srcdir下全部文件夹下的名字，以文件夹名字+数字命名'
    alldir = browse_folder(srcdir)
    for dir in alldir:
        new_filename = dir.split('\\')[-1]
        file_rename(dir, new_filename)


if __name__ == '__main__':
    path = raw_input('请输入修改的文件夹：')
    file_rename(path, 'water0')
