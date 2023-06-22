from behave import given, when, then
from behave import *
from selenium.webdriver.common.by import By

from BotanikaBeauty.pages.new_product_page import NewProductPage
from _elementtree import Element
from BotanikaBeauty.components.navigation_bar import NavigationBar
@given('Botanika Beauty page is launched')
def open_homepage(context):
    context.driver.get("https://botanikabeauty.com/")

@given('customer has selected available "{supply}" from new product page')
def open_new_product_page(context, supply):
    new_products = NewProductPage(context.browser) #?
    context.new_products = #?

    if supply == "shampoo":
        assert context.new_product_page.get_text("The Cleanser Hydrating Shampoo")
    elif supply == "conditioner":
        assert context.new_product_page.get_text("The Manager Silkening Conditioner")
    elif supply == "trio bundle":
        assert context.new_product_page.get_text("Trio Bundle:Manager,Lifter & Cleanser")
    elif supply == "spray":
        assert  context.new_product_page.get_text("The Lifter Volumizer Spray")


@when('"{quantity}" of the "{supply}" was added to the shopping cart')
def add_to_cart(context, quantity):

    if quantity == "1":
        assert context.add_to_cart_btn.click()
        assert context.cart.get_text("The '{supply}' x1")
    elif quantity == "3":
        assert context.add_to_cart_btn.click()
        assert context.cart.get_text("The '{supply}' x3")
    elif quantity == "5":
        assert context.add_to_cart_btn.click()
        assert context.cart.get_text("The '{supply}' x5")


@then('customer can see that number of products in the cart was updated')
def verify_cart_update(context):
    cart_update_message = Element(context.browser, By.XPATH,"//span[@class='js-cart-count site-header__cart-indicator']" )
   assert verify_cart_update.get_text() == "Item(s) added to cart"






