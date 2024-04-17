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

class TestTest3():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test3(self):
    self.driver.get("http://localhost:3000/home")
    self.driver.set_window_size(1552, 880)
    self.driver.find_element(By.LINK_TEXT, "diet").click()
    element = self.driver.find_element(By.LINK_TEXT, "diet")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".dietbox:nth-child(3) .row:nth-child(1) > .col-3:nth-child(2) > img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".center .position-absolute").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dietbox:nth-child(3) .row:nth-child(3) > .col-3:nth-child(1) > img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".center .position-absolute").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dietbox:nth-child(4) .row:nth-child(2) > .col-3:nth-child(1) > img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".center .position-absolute").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dietbox:nth-child(4) .row:nth-child(4) > .col-3:nth-child(3) > img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".center .position-absolute").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dietbox:nth-child(5) .row:nth-child(3) > .col-3:nth-child(2) > img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".center .position-absolute").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dietbox:nth-child(6) .row:nth-child(2) > .col-3:nth-child(1) > img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".center .position-absolute").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dietbox:nth-child(2) .row:nth-child(1) > .col-3:nth-child(1) > img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".center .position-absolute").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dietbox:nth-child(2) .row:nth-child(3) > .col-3:nth-child(2) > img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".center .position-absolute").click()
  
