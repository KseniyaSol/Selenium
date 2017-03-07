# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Untitled2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled2(self):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_id("imdbsearch").clear()
        driver.find_element_by_id("imdbsearch").send_keys("Memories of geisha")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Memories_of_geisha").click()
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("Test")
        driver.find_element_by_name("taglines").clear()
        driver.find_element_by_name("taglines").send_keys("Test")
        driver.find_element_by_name("plotoutline").clear()
        driver.find_element_by_name("plotoutline").send_keys("Test")
        driver.find_element_by_name("plots").clear()
        driver.find_element_by_name("plots").send_keys("Test")
        driver.find_element_by_id("text_languages_0").clear()
        driver.find_element_by_id("text_languages_0").send_keys("Russian")
        driver.find_element_by_name("subtitles").clear()
        driver.find_element_by_name("subtitles").send_keys("Test")
        driver.find_element_by_name("audio").clear()
        driver.find_element_by_name("audio").send_keys("Test")
        driver.find_element_by_name("video").clear()
        driver.find_element_by_name("video").send_keys("test")
        driver.find_element_by_name("country").clear()
        driver.find_element_by_name("country").send_keys("test")
        driver.find_element_by_name("genres").clear()
        driver.find_element_by_name("genres").send_keys("test")
        driver.find_element_by_name("director").clear()
        driver.find_element_by_name("director").send_keys("test")
        driver.find_element_by_name("writer").clear()
        driver.find_element_by_name("writer").send_keys("test")
        driver.find_element_by_name("producer").clear()
        driver.find_element_by_name("producer").send_keys("test")
        driver.find_element_by_name("music").clear()
        driver.find_element_by_name("music").send_keys("test")
        driver.find_element_by_name("cast").clear()
        driver.find_element_by_name("cast").send_keys("test")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_id("imdbsearch").clear()
        driver.find_element_by_id("imdbsearch").send_keys("Pobeg_iz_shoushenka")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Pobeg_iz_shoushenka").click()
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("test")
        driver.find_element_by_name("imdbid").clear()
        driver.find_element_by_name("imdbid").send_keys("test")
        driver.find_element_by_name("taglines").clear()
        driver.find_element_by_name("taglines").send_keys("test")
        driver.find_element_by_name("rating").clear()
        driver.find_element_by_name("rating").send_keys("test")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_css_selector("div.nocover").click()
        driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
        driver.find_element_by_link_text("Home").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
