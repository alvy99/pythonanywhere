import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from page import elem
from data import input


def baseLogin(driver):
    # steps
    driver.get(elem.login_url) # buka situs
    time.sleep(3)
    driver.find_element(By.XPATH, elem.email).send_keys(input.email) # isi username
    time.sleep(3)
    driver.find_element(By.XPATH, elem.password).send_keys(input.password) # isi password
    time.sleep(3)
    driver.find_element(By.XPATH, elem.btn_login ).click()
    time.sleep(3)