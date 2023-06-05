from BrainBucket.webelements.UIElement import UIElement as Element
from selenium.webdriver.support.select import Select

class Dropdown(Element):
    def __init__(self, browser, by, locator):
        super().__init__(browser, by, locator)

    def select_by_text(self, option):
        Select(self.get_element).select_by_visible_text(option)

    def select_by_value(self, value):
        Select(self.get_element).select_by_value(value)

    def select_by_index(self, index):
        Select(self.get_element).select_by_index(index)

    def select_by_option_xpath(self, option_xpath):
        self.click(self.get_locator() + option_xpath)

