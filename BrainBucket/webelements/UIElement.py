from selenium.webdriver.support import expected_conditions as EC

class UIElement:
    def __init__(self,browser,by, locator ):
        self.driver = browser.get_driver()
        self.wait = browser.get_wd_wait()
        self._locator = locator


    def get_element(self):
        return self.driver.find_element(self._)


    def wait_until_visible(self):
        return self.wait.until(EC.visibility_of_element_located((self._by, self._locator)))

    def get_text(self,wait=True):
        if wait:
            element = self.wait_until_visible()
        else:
            element = self.get_element()
        return element.text

    def get_attribute(self, attribute, wait=True):
        if wait:
            element = self.wait_until_visible()
        else:
            element = self.get_element()
        return element.get_attribute(attribute)

    def click(self):
         self.wait.until(EC.element_to_be_clickable((self._by, self._locator))).submit()

    def enter_text(self, text, wait=False):
        if wait:
            element = self.wait_until_visible()
        else:
            element = self.get_element()

        element.clear()
        element.send_keys(text)

    def submit(self):
        self.wait.until(EC.element_to_be_clickable((self._by, self._locator))).submit()

