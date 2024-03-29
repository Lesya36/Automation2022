from BrainBucket.pages.home_page import HomePage
from BrainBucket.webelements.browser import Browser
from BrainBucket.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By

URL = "http://techskillacademy.net/practice/"


def test_opening_all_desktops():
    browser = Browser(URL)
    home_page = HomePage(browser)
    home_page.show_all_desktops()

    section_title = Element(browser, By.XPATH, "//*[@id='content']/h2").get_text()
    assert section_title == "Desktops"


def test_opening_all_pcs():
    browser = Browser(URL)
    home_page = HomePage(browser)
    home_page.show_pcs()

    picture = Element(browser, By.XPATH, "//img[@title=title='Samsung SyncMaster 941BW']")
    picture.wait_until_visible()


def test_opening_all_macs():
    browser = Browser(URL)
    home_page = HomePage(browser)
    home_page.show_mac_desktops()
    text = Element(browser, By.XPATH, "//*[contains(text(),'Mac(1)')")

    print(text.get_text(wait=False))
    assert text.get_text(wait=False) == 'Mac(1)'


if "__main__" == __name__:
    test_opening_all_desktops()
    test_opening_all_pcs()
    test_opening_all_macs()
