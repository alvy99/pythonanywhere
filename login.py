import unittest
import base_login
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from page import elem
from data import input

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_success_login(self):
        # steps
        driver = self.browser #buka web browser

        base_login.baseLogin(driver)
        response_data = driver.current_url
        self.assertEqual(response_data, elem.login_url)

        
        # driver.get("https://barru.pythonanywhere.com/daftar") # buka situs
        # time.sleep(3)
        # driver.find_element(By.XPATH,elem.email).send_keys(input.email) # isi nama
        # time.sleep(3)
        # driver.find_element(By.XPATH,elem.password).send_keys(input.password) # isi nama
        # time.sleep(5)
        # driver.find_element(By.XPATH,elem.btn_login).click()
        # time.sleep(5)
        # driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        # time.sleep(1)
        # driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        # time.sleep(1)
        # driver.find_element(By.ID, "login-button").click()
        # time.sleep(1)

     # validasi
        response_data = driver.current_url
        self.assertEqual(response_data, elem.login_url)

    def test_b_failed_login_invalidemail(self):
        # steps
        driver = self.browser #buka web browser

        # base_login.baseLogin(driver)
        # response_data = driver.current_url
        # self.assertEqual(response_data, elem.login_url)

        driver.get("https://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        driver.find_element(By.XPATH,elem.email).send_keys(input.invalidemail) # isi nama
        time.sleep(3)
        driver.find_element(By.XPATH,elem.password).send_keys(input.password) # isi nama
        time.sleep(5)
        driver.find_element(By.XPATH,elem.btn_login).click()
        time.sleep(5)
        
     # validasi
        response_data = driver.find_element(By.XPATH, elem.validasi_email).text
        self.assertEqual(response_data, input.alert_eml)
        

    def test_c_failed_login_invalidpswrd(self):
            # steps
        driver = self.browser #buka web browser

        # base_login.baseLogin(driver)
        # response_data = driver.current_url
        # self.assertEqual(response_data, elem.login_url)

        driver.get("https://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        driver.find_element(By.XPATH,elem.email).send_keys(input.email) # isi nama
        time.sleep(3)
        driver.find_element(By.XPATH,elem.password).send_keys(input.invalidpassword) # isi nama
        time.sleep(5)
        driver.find_element(By.XPATH,elem.btn_login).click()
        time.sleep(5)
        
     # validasi
        response_data = driver.find_element(By.XPATH, elem.validasi_password).text
        self.assertEqual(response_data, input.alert_eml)

    def test_d_failed_login_blank(self):
            # steps
        driver = self.browser #buka web browser

        # base_login.baseLogin(driver)
        # response_data = driver.current_url
        # self.assertEqual(response_data, elem.login_url)

        driver.get("https://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        driver.find_element(By.XPATH,elem.btn_login).click()
        time.sleep(5)
        
     # validasi
        response_data = driver.find_element(By.XPATH, elem.validasi_email).text
        self.assertEqual(response_data, input.alert_eml)


def tearDown(self):
    self.browser.close()

if __name__ == "__main__":
    unittest.main()
