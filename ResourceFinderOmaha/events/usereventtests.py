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

class TestUser1Createaccount():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_user1Createaccount(self):
    self.driver.get("http://ec2-3-144-144-14.us-east-2.compute.amazonaws.com/")
    self.driver.set_window_size(1721, 927)
    self.driver.find_element(By.LINK_TEXT, "Create an account").click()
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("Test User")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("test123")
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("testuser@gmail.com")
    self.driver.find_element(By.ID, "email").send_keys(Keys.ENTER)

class TestUser2Login():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_user2Login(self):
    self.driver.get("http://ec2-3-144-144-14.us-east-2.compute.amazonaws.com/")
    self.driver.set_window_size(1721, 927)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("Test User")
    self.driver.find_element(By.ID, "password").send_keys("test123")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
  
class TestUser3Logout():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_user3Logout(self):
    self.driver.get("http://ec2-3-144-144-14.us-east-2.compute.amazonaws.com/")
    self.driver.set_window_size(1721, 927)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("Test User")
    self.driver.find_element(By.ID, "password").send_keys("test123")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
  
class TestUser4Register():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_user4Register(self):
    self.driver.get("http://ec2-3-144-144-14.us-east-2.compute.amazonaws.com/")
    self.driver.set_window_size(1721, 927)
    self.driver.find_element(By.ID, "username").send_keys("Test User")
    self.driver.find_element(By.ID, "password").send_keys("test123")
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    self.driver.find_element(By.LINK_TEXT, "My Events").click()
    self.driver.find_element(By.LINK_TEXT, "Home").click()
    self.driver.find_element(By.LINK_TEXT, "Nights at the zoo").click()
    self.driver.find_element(By.NAME, "action").click()
    self.driver.find_element(By.LINK_TEXT, "My Events").click()
  
class TestUser5Unregister():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_user5Unregister(self):
    self.driver.get("http://ec2-3-144-144-14.us-east-2.compute.amazonaws.com/")
    self.driver.set_window_size(1721, 927)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("Test User")
    self.driver.find_element(By.ID, "password").send_keys("test123")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    self.driver.find_element(By.LINK_TEXT, "My Events").click()
    self.driver.find_element(By.NAME, "action").click()