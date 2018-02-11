import aircv as ac
import os, tempfile

PATH = lambda p: os.path.abspath(p)
TEMP_FILE = PATH(tempfile.gettempdir() + "/temp_screen.png")


def get_element(imobj):
    imsrc = driver.get_screenshot_as_file(TEMP_FILE)
    pos = ac.find_template(imsrc, imobj).get('result')
    return pos


def get_screenshot(self):
    self.driver.get_screenshot_as_file(TEMP_FILE)
