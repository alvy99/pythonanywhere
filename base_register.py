import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from page import elem
from data import input


def baseRegister(driver):
    # steps
    driver.get(elem.register_url) # buka situs
    time.sleep(3)
    driver.find_element(By.XPATH, elem.btn_signup).click()
    time.sleep(3)
    driver.find_element(By.XPATH, elem.name).send_keys(input.name) # isi name
    time.sleep(3)
    driver.find_element(By.XPATH, elem.email_reg).send_keys(input.email_reg) # isi username
    time.sleep(3)
    driver.find_element(By.XPATH, elem.pswd_reg).send_keys(input.password) # isi password
    time.sleep(3)
    driver.find_element(By.XPATH, elem.btn_register).click()
    time.sleep(3)