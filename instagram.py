from suman import Confidential_Data
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Suman:
    url = "https://www.instagram.com/"
    driver = webdriver.Firefox()

    def Instagram_Login(self):
        username = Confidential_Data().insta_username
        password = Confidential_Data().insta_password
        self.driver.get(self.url)
        time.sleep(5)
        username_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
        password_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
        submit_button_xpath = '//*[@id="loginForm"]/div/div[3]'
        username1 = self.driver.find_element(by=By.XPATH, value=username_xpath)
        password1 = self.driver.find_element(by=By.XPATH, value=password_xpath)
        submit_button = self.driver.find_element(by=By.XPATH, value=submit_button_xpath)

        username1.send_keys(username)
        time.sleep(5)
        password1.send_keys(password)
        submit_button.click()


Suman().Instagram_Login()
