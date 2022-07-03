from suman import Confidential_Data
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Suman:
    url = "https://www.instagram.com/"
    driver = webdriver.Firefox()

   def Instagram_Login(self):
        username = "INSTAGRAM USERNAME"
        password = "INSTAGRAM PASSWORD"
        self.driver.get(self.url)
        time.sleep(5)
        username1 = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        password1 = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        submit_button = self.driver.find_element(by=By.XPATH, value= '//*[@id="loginForm"]/div/div[3]')
        username1.send_keys(username)
        password1.send_keys(password)
        submit_button.click()
        time.sleep(5)
        not_now = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/section/main/div/div/div/div/button')
        not_now.click()


Suman().Instagram_Login()
