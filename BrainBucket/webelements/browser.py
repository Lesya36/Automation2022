from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Browser:
    def __init__(self, url, browser_name="", time_wait = 10):
        # decide which browser to open, can be extended
        if browser_name.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--width=360")
            options.add_argument("--height=800")

            firefox_profile = webdriver.FirefoxProfile()
            firefox_profile.set_preference("browser.urlbar.showPopup", True)

            self.driver = webdriver.Firefox(firefox_profile=firefox_profile, executable_path='../drivers/geckodriver')
            self.driver.maximize_window()
        else:
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--window-size=412,915")
            options.add_argument("--incognito")
            options.add_argument("--disable-popup-blocking")
            options.add_experimental_option("excludeSwitches", ['enable-automation'])
            self.driver = webdriver.Chrome(executable_path=r'../drivers/chromedriver', options=options)

        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.implicitly_wait(time_wait)  # by default 10, but we can add this like a parameter

    def get_wd_wait(self):
        return self.wait

    def get_driver(self):
        return self.driver

    def get_email(self):
        return self.driver

    def get_password(self):
        return self.driver

    def get_width(self):
        return self.driver

    def get_length(self):
        return self.driver

    def shutdown(self):
        self.driver.quit()