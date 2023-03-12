import unittest
import base_register
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from page import elem
from data import input

class TestRegister(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_success_register(self):
        # steps
        driver = self.browser #buka web browser

        base_register.baseRegister(driver)
        response_data = driver.current_url
        self.assertEqual(response_data, elem.register_url)

     # validasi
        response_data = driver.current_url
        self.assertEqual(response_data, elem.register_url)
        

def tearDown(self):
    self.browser.close()

if __name__ == "__main__":
    unittest.main()
