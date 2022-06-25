from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# HEADLESS BROWSING

# object created for the class Options()
options = Options()

# calling a property of the class Options()
options.headless = True

# actually making it a Headless Browsing
driver = webdriver.Firefox(options=options)
print("Python Selenium Started in Headless Browsing Mode")
driver.get("https://www.google.co.in")

print(driver.title)

print(driver.current_url)

driver.close()

