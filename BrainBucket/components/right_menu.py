from BrainBucket.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class RightMenu:
    def __init__(self, browser):
        self.login_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[1]")
        self.registration_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[2]")
        self.forgotten_password_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[3]")
        self.my_account_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[4]")
        self.address_book_btn = Element(browser, By.XPATH, "//a[contains(text(),'Address Book')]")
        self.wish_list_btn = Element(browser, By.ID, "wishlist-total")
        self.order_history_btn = Element(browser, By.ID, "Order History")
        self.downloads_btn = Element(browser, By.XPATH, "//a[contains(text(),'Downloads')]")
        self.recurring_payments_btn = Element(browser, By.XPATH, "//a[contains(text(),'Recurring payments')]")
        self.reward_points_btn = Element(browser, By.XPATH, "//a[contains(text(),'Reward Points')]")
        self.returns_btn = Element(browser, By.ID, "Returns")
        self.transactions_btn = Element(browser,By.XPATH, " //a[contains(text(),'Transactions')]")
        self.newsletter_btn = Element(browser, By.ID, "Newsletter")

    def click_login(self):
        self.login_btn.click()

    def click_registration(self):
        self.registration_btn.click()

    def click_forgotten_btn(self):
        self.forgotten_password_btn.click()

    def click_my_account(self):
        self.my_account_btn.click()

    def click_address_book(self):
        self.address_book_btn.click()

    def click_wish_list(self):
        self.wish_list_btn.click()

    def click_order_history(self):
        self.order_history_btn.click()

    def click_downloads(self):
        self.downloads_btn.click()

    def click_recurring_payments(self):
        self.recurring_payments_btn.click()

    def reward_points(self):
        self.reward_points_btn.click()

    def click_returns(self):
        self.returns_btn.click()

    def click_transactions(self):
        self.transactions_btn.click()

    def click_newsletter(self):
        self.newsletter_btn.click()

