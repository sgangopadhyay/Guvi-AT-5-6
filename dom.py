import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Suman:
    driver = webdriver.Firefox()

    # use the selector ID
    def use_id(self, url, link_id):
        try:
            self.driver.get(url)
            link_id = self.driver.find_element(by=By.ID, value=link_id)
            if link_id:
                time.sleep(5)
                link_id.click()
        except:
            print("ERROR : ID not found !")

    # use the selector CLASS
    def use_class(self, url, link_class):
        try:
            self.driver.get(url)
            link_class = self.driver.find_element(by=By.CLASS_NAME, value=link_class)
            if link_class:
                time.sleep(5)
                link_class.click()
        except:
            print("ERROR : CLASS Not found !")

    # use the selector XPATH
    def use_xpath(self, url, link_xpath):
        try:
            self.driver.get(url)
            link_xpath = self.driver.find_element(by=By.XPATH, value=link_xpath)
            if link_xpath:
                time.sleep(5)
                link_xpath.click()
        except:
            print("ERROR : XPATH Not found !")

url = "https://www.w3schools.com/"

url_1 = "https://www.guvi.in/"

id_1 = "w3loginbtn12"

class_1 = "suman"

xpath_1 = '/html/body/header/nav/div/div/div[2]/div[1]/ul/li[1]/a'

# Suman().use_id(url, id_1)

# Suman().use_class(url,class_1)

Suman().use_xpath(url_1, xpath_1)

