import unittest

test_dir = r'D:\soft\pyc\test\web_test'

discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
if __name__ == '__main__':
    runer = unittest.TextTestRunner()
    runer.run(discover)
