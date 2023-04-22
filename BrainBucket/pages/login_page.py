from BrainBucket.components.header import Header
from BrainBucket.components.right_menu import RightMenu
from BrainBucket.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, browser):
        self.header = Header(browser)
        self.right_menu = RightMenu(browser)
        self.continue_btn = Element(browser, By.XPATH, "//a[contains(text(), 'Continue')]")
        self.new_customer_title = Element(browser, By.XPATH, "//h2[contains(text(), 'New Customer')]")
        self.returning_customer_title = Element(browser, By.XPATH, "//h2[contains(text(), 'Returning Customer')]")
        self.email_input = Element(browser, By.ID, "input-email")
        self.password_input = Element(browser, By.ID, "input-password")
        self.login_button = Element(browser, By.XPATH, "//input[@value='Login']")
        self.forgotten_btn = Element(browser, By.XPATH, "//a[contains(text(), 'Forgotten Password'")
        self.warning_title = Element(browser, By.XPATH, "//div[contains(text(), 'Warning: No match')]")
        self.confirmation_message = Element(browser, By.XPATH, "//div[contains(text(), 'An email with confirmation'")

    def open_registration_from_menu(self):
        self.header.open_login_btn()
        self.right_menu.click_registration()

    def open_registration_from_account_dropdown(self):
        self.header.open_registration_form()

    def click_continue_btn(self):
        self.header.open_login_btn()
        self.continue_btn.click()

    def get_new_customer_title(self):
        return self.new_customer_title.get_text()

    def get_returning_customer_title(self):
        return self.returning_customer_title.get_text()

    def enter_email(self, text):
        self.header.open_login_btn()
        self.email_input.enter_text(text)

    def enter_password(self, text):
        self.header.open_login_btn()
        self.password_input.enter_text(text)

    def click_login_button(self):
        self.header.open_login_btn()
        self.login_button.click()

    def click_forgotten_btn(self):
        self.header.open_login_btn()
        self.forgotten_btn.click()

    def get_warning_title(self):
        return self.warning_title.get_text()

    def get_confirmation_message(self):
        return self.confirmation_message.get_text()
