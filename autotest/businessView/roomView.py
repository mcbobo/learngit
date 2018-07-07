import logging
from common.common_fun import Common,NoSuchElementException
from common.desired_caps import appium_desired
# from selenium.webdriver.common.by import By

class RoomView(Common):
    friendBtn=r""
    createBtn=r""

    def create_room(self,room_type):
        self.check_updateBtn()
        self.check_loginBtn()
        self.check_sign_inBtn()

        logging.info('============create_room_action==============')
        logging.info('roomType is:%s' %room_type)
        self.find_element(room_type)

        logging.info('====start create room====')
        self.driver.find_element(self.createBtn)

        logging.info('create room finished!')

    def get_into_room(self,roomid):
        logging.info('=====get into room====')
        self.find_element(self.friendBtn)
        for i in roomid:
            self.tap_roomid(i)
        self.tap_roomid('ok')
        logging.info('tap roomid finished!')

    def check_roomStatus(self):
        logging.info('====check_loginStatus======')
        self.check_market_ad()
        self.check_account_alert()

        try:

            self.driver.find_element(*self.button_mysefl).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error('login Fail!')
            self.getScreenShot('login fail')
            return False
        else:
            logging.info('login success!')
            self.logout_action()
            return True

    def exit_room(self):
        logging.info('=====logout_action======')
        self.driver.find_element(*self.RightButton).click()
        self.driver.find_element(*self.logoutBtn).click()
        self.driver.find_element(*self.tip_commit).click()



if __name__ == '__main__':
    driver=appium_desired()
    l=RoomView(driver)
    l.login_action('自学网2018','zxw2018')
    # l.login_action('自学网2018','34454')
    l.check_loginStatus()