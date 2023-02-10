from BrainBucket.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class Footer:
    def __init__(self, browser):
        self.info_logo = Element(browser, By.XPATH, "//h5[contains('Information')]")
        self.about_us_btn = Element(browser, By.XPATH, "//a[contains('About Us')]")
        self.delivery_info_btn = Element(browser, By.XPATH, "//a[contains('Returns')]")
        self.privacy_policy_btn = Element(browser, By.XPATH, "//a[contains(text(),'Privacy Policy')]")
        self.terms_cond_btn = Element(browser, By.XPATH, "//a[contains(text(),'Terms & Conditions')]")
        self.customer_service_title_btn = Element(browser, By.XPATH, "//h5[contains('Customer Service')]")
        self.contact_us_btn = Element(browser, By.XPATH, "//a[contains(text(),'Contact Us')]")
        self.returns_btn = Element(browser, By.XPATH, "//a[contains(text(),'Returns')]")
        self.site_map = Element(browser, By.XPATH, " //a[contains(text(),'Site Map')]")
        self.extras_title_btn = Element(browser, By.XPATH, "//h5[contains(text(),'Extras')]")
        self.brands_btn = Element(browser, By.XPATH, "//a[contains(text(),'Brands')]")
        self.gift_certificate_btn = Element(browser, By.XPATH, "//a[contains(text(),'Gift Certificates')]")
        self.affiliates_btn = Element(browser, By.XPATH, " //a[contains(text(),'Affiliates')]")
        self.specials_btn = Element(browser, By.XPATH, "//a[contains(text(),'Specials')]")
        self.my_acc_title_btn = Element(browser, By.XPATH, "//h5[contains('Order History')]")
        self.order_history_btn = Element(browser, By.XPATH, "//a[contains(text(),'Order History')]")
        self.wish_list_btn = Element(browser, By.XPATH, "//a[contains(text(),'Wish List')]")
        self.newsletter_btn = Element(browser, By.XPATH, "//a[contains(text(),'Newsletter')]")

    def info_logo_is_visible(self):
        return self.info_logo.wait_until_visible()

    def click_about_us_btn(self):
        self.about_us_btn.click()

    def click_delivery_info(self):
        self.delivery_info_btn.click()

    def click_privacy_policy_btn(self):
        self.privacy_policy_btn.click()

    def click_terms_cond_btn(self):
        self.terms_cond_btn.click()

    def click_customer_service_title_btn(self):
        self.customer_service_title_btn.click()

    def click_contact_us_btn(self):
        self.contact_us_btn.click()

    def click_returns_btn(self):
        self.returns_btn.click()

    def click_site_map(self):
        self.site_map.click()

    def click_extras_title_btn(self):
        self.extras_title_btn.click()

    def click_brands_btn(self):
        self.brands_btn.click()

    def click_gift_certificate_btn(self):
        self.gift_certificate_btn.click()

    def click_affiliates_btn(self):
        self.affiliates_btn.click()

    def click_specials_btn(self):
        self.specials_btn.click()

    def verify_my_acc_title_btn_is_visible(self):
        return self.my_acc_title_btn.click()

    def click_order_history_btn(self):
        self.order_history_btn.click()

    def click_wish_list_btn(self):
        self.wish_list_btn.click()

    def click_newsletter_btn(self):
        self.newsletter_btn.click()

