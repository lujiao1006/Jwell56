# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, sys
import logging
from userlib import userlib


class YouddDao(unittest.TestCase):
    globalpath = sys.path[4]
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.base_url = "https://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        userlib.Userlib().initallog(self.globalpath)


    def test_case(self):
        logging.info("Start")
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.baidu.com")
        userlib.Userlib().sceenshot(driver, self.globalpath)
        try:
            print  "012"
            driver.find_element_by_id("k5w").click()
            driver.find_element_by_id("kw").clear()
            driver.find_element_by_id("kw").send_keys("python")
            driver.find_element_by_id("su").click()
        finally:
            userlib.Userlib().sceenshot(driver, self.globalpath)
            # print self.globalpath,userlib.Userlib().getpath()





    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
