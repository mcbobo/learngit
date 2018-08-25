import logging

username = '13726221317'
pwd = 'zmjj123456'

logging.info('============login_action==============')
driver.find_element_by_id('com.tencent.mm:id/d75').click()
driver.find_element_by_id('com.tencent.mm:id/hz').send_keys(username)
driver.find_element_by_id('com.tencent.mm:id/alr').click()
driver.find_element_by_id('com.tencent.mm:id/hz').send_keys(pwd)
driver.find_element_by_id('com.tencent.mm:id/alr').click()
