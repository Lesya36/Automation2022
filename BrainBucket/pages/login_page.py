from BrainBucket.components.header import Header
from BrainBucket.components.right_menu import RightMenu
from BrainBucket.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, browser):
        self.header = Header(browser)
        self.right_menu = RightMenu(browser)
        self.continue_btn = Element(browser, By.XPATH, "//a[contains(text(), 'Continue')]")
        self.input_email = Element(browser, By.XPATH, "//input[@id='input-email']")
        self.input_password = Element(browser, By.XPATH, " //input[@id='input-password']")
        self.login_btn = Element(browser, By.ID, "Login")

    def open_registration_from_menu(self):
        self.header.open_login_page()
        self.right_menu.click_registration()

    def open_registration_from_account_dropdown(self):
        self.header.open_registration_form()

    def click_continue_btn(self):
        self.header.open_login_page()
        self.continue_btn.click()

    def input_email(self, text):
        self.header.open_login_page()
        self.input_email.enter_text(text)

    def input_password(self, text):
        self.header.open_login_page()
        self.input_password.enter_text(text)

    def login_btn(self):
        self.header.open_login_page()
        self.login_btn.click()
