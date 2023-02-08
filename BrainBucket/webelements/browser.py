from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait



class Browser:
    def __init__(self, url, browser_name = ""):
        if browser_name.lower() == "chrome":
            self.driver = webdriver.Chrome(executable_path="webelements/chromedriver.exe")

        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def get_wd_wait(self):
        return self.wait

    def get_driver(self):
        return self.driver

    def shutdown(self):
        self.driver.quit()