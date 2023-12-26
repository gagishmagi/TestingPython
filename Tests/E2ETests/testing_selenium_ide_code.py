# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestDefaultSuite():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        # self.driver = webdriver.Edge()
        # self.driver = webdriver.Ie()
        self.vars = {}
        self.driver.get("https://www.google.com/")
        self.driver.set_window_size(1162, 607)

    def teardown_method(self, method):
        self.driver.quit()

    def test_testingSearchforQAautomation(self):
        time.sleep(10)
        # self.driver.save_screenshot("image.png")
        assert self.driver.title == "Google"

        # self.driver.find_element(By.ID, "APjFqb").click()
        # element = self.driver.find_element(By.CSS_SELECTOR, ".gb_Aa")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # element = self.driver.find_element(By.CSS_SELECTOR, "body")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element, 0, 0).perform()
        # element = self.driver.find_element(By.CSS_SELECTOR, "#gbwa .gb_d")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # element = self.driver.find_element(By.CSS_SELECTOR, "body")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element, 0, 0).perform()
        self.driver.close()

    def test_testingSearchforQAautomation2(self):
        inputbox = self.driver.find_element(By.NAME,"q")
        inputbox.click()
        inputbox.send_keys("QA Automation Engineer")
        inputbox.send_keys(Keys.ENTER)
        # self.driver.find_element(By.NAME,"q")
        time.sleep(5)

        # links = self.driver.find_elements(By.CSS_SELECTOR,"a")
        links = self.driver.find_elements(By.CSS_SELECTOR,"h3")
        # for link in links:
        #     print(link.text)
            # assert link.text == "111 Qa Automation Engineer jobs in Israel (1 new)"

        assert links[0].text == "111 Qa Automation Engineer jobs in Israel (1 new)"
        links[0].click()
        time.sleep(5)

        # self.driver.find_element(By.ID, "APjFqb").click()
        # element = self.driver.find_element(By.CSS_SELECTOR, ".gb_Aa")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # element = self.driver.find_element(By.CSS_SELECTOR, "body")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element, 0, 0).perform()
        # element = self.driver.find_element(By.CSS_SELECTOR, "#gbwa .gb_d")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # element = self.driver.find_element(By.CSS_SELECTOR, "body")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element, 0, 0).perform()
        self.driver.close()
