# coding:utf-8
from BasePage import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class DailyMtt(Page):
    '''日常赛事创建'''

    url = 'MatchManage/index.html'

    # 定位器
    createbutton_loc = (By.XPATH, '/html/body/div[1]/div/div/div/a')
    name_loc = (By.ID, 'add_match_name')
    time_loc = (By.ID, 'add_match_time')
    stime_loc = (By.ID, 'add_match_time')
    sdate_loc = (By.ID, 'add_match_date')
    edate_loc = (By.ID, 'add_end_date2')
    pnum1_loc = (By.ID, 'add_people_num1')
    pnum2_loc = (By.ID, 'add_people_num2')
    price_loc = (By.ID, 'add_price_num')
    exit_time_loc = (By.ID, 'add_for_exit_time')
    enrollTime_loc = (By.XPATH, '/html/body/div[2]/div/div/div[2]/form/div[12]/div[1]/div/input')
    price_model_loc = (By.XPATH, '/html/body/div[2]/div/div/div[2]/form/div[11]/div[1]/div/input')
    save_loc = (By.ID, 'save')
    reword_xlsx_path = r'D:\OneKeyBak\backup\desktop\000.xlsx'

    def type_createbutton(self):
        self.find_element(*self.createbutton_loc).click()

    def type_name(self):
        match_name = datetime.datetime.now().time()
        self.find_element(*self.name_loc).send_keys(match_name)

    def type_start_time(self, time_delay):
        match_time = self.get_statr_time(time_delay)
        self.find_element(*self.stime_loc).send_keys(match_time)

    def type_sdate(self):
        start_date = str(datetime.datetime.now().date())
        self.find_element(*self.sdate_loc).send_keys(start_date)

    def type_edate(self):
        end_date = (datetime.datetime.now() + datetime.timedelta(days=1)).date()
        self.find_element(*self.sdate_loc).send_keys(end_date)

    def type_other_num(self):
        '默认输入人数范围2~5，奖励1000金币，退出时间3分钟,报名时间1小时，奖励表000'
        self.find_element(*self.pnum1_loc).send_keys('2')
        self.find_element(*self.pnum2_loc).send_keys('5')
        self.find_element(*self.price_loc).send_keys('1000')
        self.find_element(*self.exit_time_loc).send_keys('5')
        self.find_element(*self.enrollTime_loc).send_keys('1')
        self.find_element(*self.price_model_loc).send_keys(self.reword_xlsx_path)

    def type_bugcs(self):
        select = Select(self.driver.find_element_by_css_selector("[name='add_cgcs']"))
        select.select_by_visible_text("1")
        select = Select(self.driver.find_element_by_css_selector("[name='add_jgcs']"))
        select.select_by_visible_text("1")

    def type_save(self):
        self.find_element(*self.save_loc).click()

def test_create_dailymtt(driver,time_delay):
    dailymtt_page = DailyMtt(driver)
