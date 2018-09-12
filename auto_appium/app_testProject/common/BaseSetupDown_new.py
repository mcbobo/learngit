# coding:utf-8
from common.BaseRunner import ParametrizedTestCase as pt
from common.BaseYaml import getMultiYam
from PageObject.Home.FirstOpenPage import FirstOpenPage


class UpDown(pt):
    @classmethod
    def setUpClass(cls):
        super(UpDown, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(UpDown, cls).tearDownClass()

    def template(self, case_name='', *args):
        # 用例模板，参数化后，可以遍历文件夹传入文件名，跑文件夹下的全部用例
        data = getMultiYam(*args)
        app = {"logTest": self.logTest, "driver": self.driver, "data": data,
               "device": self.devicesName, "caseName": case_name}

        page = FirstOpenPage(app)
        page.operate()
        page.checkPoint()
