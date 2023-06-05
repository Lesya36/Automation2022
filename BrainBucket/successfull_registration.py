from selenium.webdriver.common.by import By
import time

from BrainBucket.webelements.browser import Browser
from BrainBucket.webelements.UIElement import UIElement as Element
from BrainBucket.webelements.dropdown import Dropdown

from BrainBucket.components.header import Header
from BrainBucket.components.right_menu import RightMenu
from BrainBucket.pages.login_page import LoginPage
from BrainBucket.pages.registration_page import RegistrationPage
from BrainBucket.utils.config_reader import ConfigReader


URL = "https://techskillacademy.net/brainbucket"
configs = ConfigReader("config.ini")


def test_registration_through_dropdown():
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
    login_page = LoginPage(browser)
    login_page.open_registration_from_account_dropdown()

    registration_form = RegistrationPage(browser)
    assert registration_form.get_form_title() == 'Register Account'

    registration_form.enter_first_name("Lesya")
    registration_form.enter_last_name("Khmelovska")
    registration_form.enter_email("lesyak1group@gmail.com")
    registration_form.enter_telephone("224-422-8196")
    registration_form.enter_first_line_address("1004 Emerald dr")
    registration_form.enter_city("Schaumburg")
    registration_form.select_state("Illinois")
    registration_form.enter_password("15865847")
    registration_form.confirm_password("15865847")
    registration_form.subscribe_to_newsletters()
    registration_form.agree_to_privacy_policy()

    registration_form.submit_form()

    successful_registration_title = Element(browser, By.XPATH, "//*[@id='content']/h1")
    assert successful_registration_title.get_text() == 'Your Account Has Been Created!'

    successful_registration_subtitle = Element(browser, By.XPATH, "//*[@id='content']/p")
    assert successful_registration_subtitle.get_text() == 'Congratulations! Your new account has been successfully created!'

    time.sleep(5)
    browser.shutdown()

def test_registration_from_right_menu():
    browser = Browser(URL)
    driver = browser.get_driver()

    # in Account dropdown select Login option
    header = Header(browser)
    header.open_login_btn()

    # click on Register btn in the right menu
    right_menu = RightMenu(browser)
    right_menu.click_registration()

    registration_form_title = Element(browser, By.XPATH, "//*[@id='content']/h1")
    assert registration_form_title.get_text() == 'Register Account'

    inputs = {
        'firstname': "Lesya",
        'lastname': "Khemelovska",
        'email': "lesyak1group@gmail.com",
        'telephone': "224-422-8196",
        'fax': "224-422-8196",
        'address_1': "1004 Emerald dr",
        'city': "Schaumburg",
        'password': "15865847",
        'confirm': "15865847"
    }

    for field, text in inputs.items():
        input_field = driver.find_element_by_name(field)
        input_field.clear()
        input_field.send_keys(text)

    # find dropdown element for Country
    Dropdown(browser, By.ID, 'input-country').select_by_text("United States")

    # find dropdown element for Region
    Dropdown(browser, By.NAME, 'zone_id').select_by_text("Illinois")

    # clicking on subscribe YES radio button
    subscribe_btn = driver.find_element_by_xpath("//input[@name='newsletter' and @value='1']")
    if not subscribe_btn.is_selected():
        subscribe_btn.click()

    driver.find_element_by_name("agree").click()

    Element(browser, By.XPATH, "//input[@value='Continue']").submit()

    successful_registration_title = Element(browser, By.XPATH, "//*[@id='content']/h1")
    assert successful_registration_title.get_text() == 'Your Account Has Been Created!'

    successful_registration_subtitle = Element(browser, By.XPATH, "//*[@id='content']/p")
    assert successful_registration_subtitle.get_text() == 'Congratulations! Your new account has been successfully created!'

    time.sleep(5)
    browser.shutdown()


if __name__ == "__main__":
    test_registration_through_dropdown()
    # test_registration_from_right_menu()