from behave import *
from selenium.webdriver.common.by import By

from BotanikaBeauty.pages.new_product_page import NewProductPage
from BrainBucket.webelements.browser import Browser


@given('Botanika Beauty page is launched')
def open_homepage(context):
    browser = Browser("https://botanikabeauty.com/", browser_name='chrome')
    context.browser = browser


@given('customer has selected available "{supply}" from new product page')
def open_new_product_page(context, supply):
    # add before that a code that opens newproduct page from homepage
    new_products = NewProductPage(context.browser)
    context.new_products = new_products

    if supply == "shampoo":
        context.new_products.add_to_cart_shampoo()
    elif supply == "conditioner":
        context.new_products.add_to_cart_conditioner()
    elif supply == "trio bundle":
        context.new_products.add_to_cart_trio_bundle()
    elif supply == "spray":
        context.new_products.add_to_cart_volumizer_spray()


@when('one  "{supply}" was added to the shopping cart')
def add_to_cart(context, supply):
    add_supply_to_cart = NewProductPage(context.browser)
    context.add_supply_to_cart = add_supply_to_cart

    if supply == "shampoo":
        context.add_supply_to_cart.add_to_cart_shampoo()
    elif supply == "conditioner":
        context.add_supply_to_cart.add_to_cart_conditioner()
    elif supply == "trio bundle":
        context.add_supply_to_cart.add_to_cart_trio_bundle()
    elif supply == "spray":
        context.add_supply_to_cart.add_to_cart_volumizer_spray()




@then('verify is in the cart')
def verify_product_in_cart(context):
    cart_update_message = Element(context.browser, By.XPATH, "//span[@class='js-cart-count site-header__cart-indicator']")
    assert cart_update_message.get_text() == "Item(s) added to cart"



