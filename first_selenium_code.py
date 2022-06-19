from selenium import webdriver

# Open a Firefox Browser in Python Selenium
def Suman_Firefox(url):
    driver = webdriver.Firefox()
    return driver.get(url)


# Open a Chrome Browser in Python Selenium
def Suman_Chrome(url):
    driver = webdriver.Chrome()
    return driver.get(url)

# open a Edge Browser in Python Selenium
def Suman_Edge(url):
    driver =  webdriver.Edge()
    return driver.get(url)

url = "https://www.guvi.in"

Suman_Edge(url)



