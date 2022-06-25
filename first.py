from selenium import webdriver

class Suman:
    driver = webdriver.Firefox()

    # fetch the title of the webpage
    def fetch_title(self, url):
        self.driver.get(url)
        return self.driver.title

    # URL of the webpage
    def fetch_url(self, url):
        self.driver.get(url)
        return self.driver.current_url

    # fetch the entite content of the webpage
    def fetch_webpage(self,url):
        self.driver.get(url)
        return self.driver.page_source


url = "https://www.google.com"

# print(Suman().fetch_title(url))

# print(Suman().fetch_url(url))

print(Suman().fetch_webpage(url))
