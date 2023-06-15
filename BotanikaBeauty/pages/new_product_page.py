
from BrainBucket.SmokeTest import browser
from BrainBucket.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By

from BrainBucket.webelements.actions import Actions


#URL = "https://botanikabeauty.com/collections/new"



class NewProductPage:
    def __init__(self, browser):
        self.actions = Actions(browser)
        self.shampoo = Element(browser,By.XPATH,"//a[contains(text(),'The Cleanser Hydrating Shampoo')]")
        self.conditioner  = Element(browser,By.XPATH,"//a[contains(text(),'The Manager Silkening Conditioner')]")
        self.trio_bundle = Element(browser,By.XPATH,"//a[contains(text(),'Trio Bundle: The Manager, Lifter & Cleanser')]")
        self.volumizer_spray = Element(browser,By.XPATH,"//a[contains(text(),'The Lifter Volumizer Spray')]")
        #shop options
        # is it possible to make them as add to cart OR quick_shop option?
        self.add_to_cart_btn = Element(browser,By.NAME,"Add to Cart") #(//span[@title='Add to Cart'])[1]
        self.quick_shop_btn = Element(browser,By.NAME,"icon-quickview") #//span[@data-handle='the-cleanser']//i[@class='icon-quickview']



     def add_to_cart_shampoo(self):
       self.actions.move_to_element(self.shampoo)
       self.add_to_cart_btn.click()

    def add_to_cart_conditioner(self):
        self.actions.move_to_element(self.conditioner)
        self.add_to_cart_btn.click()

    def add_to_cart_trio_bundle(self):
        self.actions.move_to_element(self.trio_bundle)
        self.add_to_cart_btn.click()

    def add_to_cart_volumizer_spray(self):
        self.actions.move_to_element(self.volumizer_spray)
        self.add_to_cart_btn.click()


    def quick_shop_shampoo(self):
        self.actions.move_to_element(self.shampoo)
        self.quick_shop_btn.click()

    def quick_shop_conditioner(self):
        self.actions.move_to_element(self.conditioner)
        self.quick_shop_btn.click()

    def quick_shop_trio_bundle(self):
        self.actions.move_to_element(self.conditioner)
        self.quick_shop_btn.click()

    def quick_shop_volumizer_spray(self):
        self.actions.move_to_element(self.volumizer_spray)
        self.quick_shop_btn.click()











