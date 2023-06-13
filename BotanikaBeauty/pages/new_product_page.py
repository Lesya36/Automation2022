
from BrainBucket.webelements.actions import Actions
from BrainBucket.webelements.browser import Browser
from BrainBucket.webelements.UIElement import UIElement
from selenium.webdriver.common.by import By
from BotanikaBeauty.components.navigation_bar import NavigationBar

URL = "https://botanikabeauty.com/collections/new"


#Yes, you need to start with xpath and creating UIElements for them inside init



class NewProductPage:
    def __init__(self, browser):
        self.actions = Actions(browser)
        self.shampoo = Element(browser,By.XPATH "//a[contains(text(),'The Cleanser Hydrating Shampoo')]")
        self.conditioner  = Element(browser,By.XPATH "//a[contains(text(),'The Manager Silkening Conditioner')]")
        self.trio_bundle = ELement(browser,By.XPATH "//a[contains(text(),'Trio Bundle: The Manager, Lifter & Cleanser')]")
        self.volumizer_spray = Element(browser,By.XPATH "//a[contains(text(),'The Lifter Volumizer Spray')]")
        #shop options
        # is it possible to make them as add to cart OR quick_shop option?
        self.add_to_cart_btn = ELement(browser,By.NAME "Add to Cart")
        self.quick_shop_btn = Element(browser,By.NAME "icon-quickview")



   def shop_shampoo(self):
       self.actions.move_to_element() # not sure if this is correct
       self.add_to_cart_btn.wait_untill_visible()
       self.add_to_cart_btn.click()

   def shop_conditioner(self):
        self.actions.move_to_element()
        self.add_to_cart_btn.wait_until_visible()
        self.add_to_cart_btn.click()


    #will continue after the rest after fix all mistakes
    def shop_trio_bundle(self):
    pass


    #should I also create same functions for each product but put
    #self.quick_shop_btn.click?











