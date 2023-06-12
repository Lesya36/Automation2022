
from BrainBucket.SmokeTest import browser
from BrainBucket.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By

from BrainBucket.webelements.actions import Actions
from BrainBucket.webelements.dropdown import Dropdown
from BrainBucket.webelements.browser import Browser



class NavigationBar:
    def __init__(self, browser):
        self.actions = Actions(browser)

        self.shop = Element(browser, By.XPATH, "//span[contains(text(),'Shop')]")
        self.cart = Element(browser, By.XPATH, "//span[@title='Shopping Cart']")

    # Dropdowns

        self.new_product_dropdown = Dropdown(browser, By.XPATH, "//a[contains(text(), 'NEW Products')]")

    def shop_new_products(self):
        self.actions.move_to_element(self.new_product_dropdown)
        self.new_product_dropdown.click()



    #def cart.update(self)

    #def cart.checkout(self)