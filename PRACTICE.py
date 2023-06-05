class Browser:
    def __init__(self, url, browser_name = "",time_wait=10):
        try:
            if browser_name.lower() == "chrome":
                self.driver = webdriver.Chrome(executable_path='BrainBucket/drivers/chromedriver.exe')
            else:
                self.driver = webdriver.Firefox(executable_path='BrainBucket/drivers/geckodriver.exe')

        except WebDriverException:
            print("Error: executable path to driver is incorrect")
            quit()

        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.maximize_window()
        self.driver.implicitly_wait(time_wait)

    def get_wd_wait(self):
        return self.wait

    def get_driver(self):
        return self.driver

    def shutdown(self):
        self.driver.quit()