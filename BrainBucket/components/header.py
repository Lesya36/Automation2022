from BrainBucket.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class Header:
    def __init__(self, browser):
        self.my_account_btn = Element(browser, By.XPATH, "//a[@title='My Account']")
        self.my_account_dropdown = Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']")
        self.register_btn = Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']/li[1]")
        self.login_btn = Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']/li[2]")
        self.wish_list_btn = Element(browser, By.ID, "wishlist-total")
        self.shopping_list_btn = Element(browser, By.XPATH, "//a[@title='Shopping Cart']")
        self.checkout_btn = Element(browser, By.XPATH, "//a[@title='Checkout']")
        self.currency_btn = Element(browser, By.ID, "form-currency")
        self.logo = Element(browser, By.ID, "logo")
        self.search_btn = Element(browser, By.ID, "search")
        self.new_currency_dropdown = Element(browser, By.XPATH, "//ul[@class = 'dropdown-menu']")
        self.euro_currency_btn = Element(browser, By.NAME, "EUR")
        self.gbp_currency_btn = Element(browser, By.NAME, "GBP")
        self.usd_currency_btn = Element(browser, By.NAME, "USD")

    def verify_logo_is_visible(self):
        return self.logo.wait_until_visible()

    def open_registration_form(self):
        self.my_account_btn.click()

    def open_login_btn(self):
        self.login_btn.click()

    def change_currency(self, new_currency):
        self.currency_btn.click()
        self.currency_btn.wait_until_visible()
        if new_currency == "USD":
            self.usd_currency_btn.click()

        elif new_currency == "GBP":
            self.gbp_currency_btn.click()

        elif new_currency == "EUR":
            self.euro_currency_btn.click()

    def open_wishlist(self):
        self.wish_list_btn.click()

    def search_for(self, text):
        self.search_btn.wait_until_visible()
        self.search_btn.enter_text(text)
        self.search_btn.click()
