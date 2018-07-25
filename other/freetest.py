# coding:utf-8
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)


class Model(dict):
    __metaclass__ = ModelMetaclass
    print 'Done'


class YeahTest(object):
    def aa(self):
        flag = 0
        while flag < 3:
            try:
                pos = 3 / flag
            except ZeroDivisionError:
                flag += 1
                sleep(1)
            else:
                # break
                return pos
        raise NoSuchElementException('can not find element')


yang = YeahTest().aa()
print yang
