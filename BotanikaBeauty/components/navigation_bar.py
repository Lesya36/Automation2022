from BrainBucket.SmokeTest import browser
from BrainBucket.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By

from BrainBucket.webelements.actions import Actions


class NavigationBar:
    def __init__(self):
        self.actions = Actions(browser)
        self.shop = Element(browser, By.XPATH, "//span[contains(text(),'Shop')]")
        self.cart = Element(browser, By.XPATH, "//span[@title='Shopping Cart']")

        # Dropdowns

        self.new_product_option = Element(browser, By.XPATH, "//a[contains(text(), 'NEW Products')]")

    def open_shop_new_products(self):
        self.actions.move_to_element(self.shop)
        self.new_product_option.click()
