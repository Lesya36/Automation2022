""" Given user launched login page
    Given user is not logged in 
    When user enters email and password 
    And user clicks Login button 
    Then user's profile page will be launched
    """
from _elementtree import Element
from behave import given, when, then
from selenium.webdriver.common.by import By

from BrainBucket.pages.login_page import LoginPage
from BrainBucket.pages.profile_page import ProfilePage
from BrainBucket.components.right_menu import RightMenu
from BrainBucket.utils.config_reader import ConfigReader
from BrainBucket.webelements.browser import Browser

URL = "https://cleveronly.com/brainbucket/index.php?route=account/login"

configs = ConfigReader("BrainBucket/BDDBehave/logintests/steps/config.ini")


@given("user launch login page")
def launch_login_page(context):
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
    context.browser = browser


@given("user is not logged in")
def verify_user_not_logged_in(context):
    login_page = LoginPage(context.browser)
    assert login_page.get_new_customer_title() == "New Customer"
    assert login_page.get_returning_customer_title() == "Returning Customer"
    context.login_page = login_page


@given("user clicks 'Forgotten Password'")
def click_forgotten_btn(context):
    login_page = context.login_page
    login_page.click_forgotten_btn()


@when("user enters email and password")
def enter_email_and_password(context):
    login_page = context.login_page
    configs = context.configs
    login_page.enter_email(configs.get_user1_email())
    login_page.enter_password(configs.get_user1_password())
    context.execute_steps()


@when('user clicks Login button')
def click_login_button(context):
    login_page = context.login_page
    login_page.click_login_button()


@then("user's profile page is launched")
def verify_user_profile_view(context):
    profile_page = ProfilePage(context.browser)
    assert profile_page.get_my_account_title() == "My Account"
    assert profile_page.get_my_orders_title() == "My Orders"
    assert profile_page.get_newsletter_title() == "Newsletter"


@when("user enters email")
def enter_email(context):
    login_page = context.login_page
    login_page.enter_email(context.configs.get_user1_email())


@when("user enters password")
def enter_password(context):
    login_page = context.login_page
    login_page.enter_password(context.configs.get_user1_password())


@then("user clicks Continue button")
def click_continue_btn(context):
    login_page = context.login_page
    login_page.click_continue_btn()


@then("warning is shown 'No match for E-Mail Address and/or Password'")
def verify_warning(context):
    warning_title = Element(context.browser, By.XPATH, "//div[contains(text(), 'Warning: No match')]")
    assert warning_title.get_text() == "warning is shown: 'No match for E-Mail Address and/or Password'"


@then("confirmation message is shown 'An email with a confirmation link has been sent your email address'")
def verify_email_sent(context):
    confirmation_message = Element(context.browser, By.XPATH, "//div[contains(text(), 'An email with confirmation'")
    assert confirmation_message.get_text() == "An email with a confirmation link has been sent your email address"
