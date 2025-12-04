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

class TestOrg1Createaccount():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_org1Createaccount(self):
    self.driver.get("http://ec2-3-144-144-14.us-east-2.compute.amazonaws.com/")
    self.driver.set_window_size(1721, 927)
    self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(5) > a").click()
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("Test Org")
    self.driver.find_element(By.ID, "desc").click()
    self.driver.find_element(By.ID, "desc").send_keys("Test organization")
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("Test Org")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("test321")
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("testorg@gmail.com")
    self.driver.find_element(By.ID, "phone").click()
    self.driver.find_element(By.ID, "phone").send_keys("4020000000")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()

class TestOrg2Login():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_org2Login(self):
    self.driver.get("http://ec2-3-144-144-14.us-east-2.compute.amazonaws.com/")
    self.driver.set_window_size(1721, 927)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("Test Org")
    self.driver.find_element(By.ID, "password").send_keys("test321")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()

class TestOrg3Logout():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_org3Logout(self):
    self.driver.get("http://ec2-3-144-144-14.us-east-2.compute.amazonaws.com/")
    self.driver.set_window_size(1721, 927)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("Test Org")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("test321")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()

class TestOrg4Createevent():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_org4Createevent(self):
    self.driver.get("http://ec2-3-144-144-14.us-east-2.compute.amazonaws.com/")
    self.driver.set_window_size(1721, 927)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("Test Org")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("test321")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    self.driver.find_element(By.LINK_TEXT, "My Events").click()
    self.driver.find_element(By.LINK_TEXT, "New Event").click()
    self.driver.find_element(By.ID, "id_title").click()
    self.driver.find_element(By.ID, "id_title").send_keys("Test event for org")
    self.driver.find_element(By.ID, "id_description").click()
    self.driver.find_element(By.ID, "id_description").send_keys("This is a test event")
    self.driver.find_element(By.ID, "id_start_at").click()
    self.driver.find_element(By.ID, "id_start_at").click()
    self.driver.find_element(By.ID, "id_start_at").click()
    self.driver.find_element(By.ID, "id_start_at").send_keys("2025-12-10T12:00")
    self.driver.find_element(By.ID, "id_end_at").click()
    self.driver.find_element(By.ID, "id_end_at").click()
    self.driver.find_element(By.ID, "id_end_at").send_keys("2025-12-10T12:30")
    self.driver.find_element(By.ID, "id_location").click()
    self.driver.find_element(By.ID, "id_location").send_keys("Omaha")
    self.driver.find_element(By.ID, "id_url").click()
    self.driver.find_element(By.ID, "id_url").send_keys("http")
    self.driver.find_element(By.ID, "id_url").send_keys(Keys.DOWN)
    self.driver.find_element(By.ID, "id_url").send_keys("https://orgtest.com")
    self.driver.find_element(By.ID, "id_capacity").click()
    self.driver.find_element(By.ID, "id_capacity").send_keys("100")
    self.driver.find_element(By.CSS_SELECTOR, ".form-field:nth-child(9)").click()
    dropdown = self.driver.find_element(By.ID, "id_categories")
    dropdown.find_element(By.XPATH, "//option[. = 'Cultural']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".register-button:nth-child(1)").click()

class TestOrg5Editevent():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_org5Editevent(self):
    self.driver.get("http://ec2-3-144-144-14.us-east-2.compute.amazonaws.com/")
    self.driver.set_window_size(1721, 927)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("Test Org")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("test321")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    self.driver.find_element(By.LINK_TEXT, "My Events").click()
    self.driver.find_element(By.LINK_TEXT, "Test event for org").click()
    self.driver.find_element(By.ID, "id_description").click()
    self.driver.find_element(By.ID, "id_description").send_keys("This is a test event, but edited")
    self.driver.find_element(By.ID, "id_title").click()
    self.driver.find_element(By.ID, "id_title").click()
    self.driver.find_element(By.ID, "id_title").send_keys("Test event")
    self.driver.find_element(By.CSS_SELECTOR, ".form-field:nth-child(2)").click()
    dropdown = self.driver.find_element(By.ID, "id_categories")
    dropdown.find_element(By.XPATH, "//option[. = 'Health']").click()
    self.driver.find_element(By.ID, "id_is_free").click()
    self.driver.find_element(By.ID, "id_location").send_keys("Omaha")
    self.driver.find_element(By.CSS_SELECTOR, ".form-field:nth-child(10)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".register-button:nth-child(1)").click()

  
