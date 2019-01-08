import unittest
from modle.driver import Chrome
from selenium import webdriver


class MyTest(unittest.TestCase):

    def setUp(self):
        d = Chrome()
        self.driver = d.browser_chrome()
    def tearDown(self):
        self.driver.quit()

