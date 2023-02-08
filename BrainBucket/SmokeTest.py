import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.select import Select
# imports for selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
# browser
from BrainBucket.webelements.browser import Browser
from BrainBucket.webelements.UIElement import UIElement as Element
from BrainBucket.webelements.dropdown import Dropdown
from BrainBucket.webelements.checkbox import Checkbox


driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

browser = Browser("https://techskillacademy.net/brainbucket")
driver = browser.get_driver()

#in Account dropdown select Register option

account_btn = Element(Browser, By.XPATH,"//a[@title='My Account']")
account_btn.click()

#wd wait till DropDown will open
Element(Browser, By.XPATH, "//*[@class=dropdown-menu dropdown-menu-right']").wait_until_visible()

#select Reqistration option
Element(Browser, By.XPATH, "//*[@class=dropdown-menu dropdown-menu-right']").wait_until_visible()
driver.find_element_by_xpath("//*[@id='colum-right']//a[2]").click()


# logo = wd_wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@title='Brainbucket']")))

new_registrant_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Continue')]")))

#background_color = new_registrant_btn.value_of_css_property("background-color")
#converted_background_color = Color.from_string(background_color)
#assert converted_background_color.rgb == 'rgb(34, 154, 200)'
#new_registrant_btn.click()


registration_from_title = Element(Browser, By.XPATH, "//div[@id= 'content']/h1" )
assert registration_from_title.get_text() == 'Register Account'



firstname_field = Element(Browser, By.XPATH, "//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class
firstname_input = Element(Browser, By.ID, "input-firstname")
firstname_input.enter_text("Lesya")


lastname_field = Element(Browser, By.XPATH, "//fieldset/div[3]")
lastname_field_class = lastname_field.get_attribute("class")
assert "required" in lastname_field_class
lastname_input = Element(Browser, By.ID, "input-lastname")
lastname_input.enter_text("Khmelovska")


email_field = Element(Browser, By.XPATH, "//fieldset/div[4]")
email_field_class = email_field.get_attribute("class")
assert "required" in email_field_class
email_input = Element(Browser, By.ID, "input-email")
email_input.enter_text("lesyak1group@gmail.com")


telephone_field = Element(Browser, By.XPATH, "//fieldset/div[5]")
telephone_field_class = telephone_field.get_attribute("class")
assert "required" in telephone_field_class
telephone_input = Element(Browser, By.ID, "input-telephone")
telephone_input.enter_text("224-422-8196")


fax_field = Element(Browser, By.XPATH, "//fieldset/div[6]")
fax_field_class = fax_field.get_attribute("class")
assert "required" not in fax_field_class
fax_input = Element(Browser, By.ID, 'input-fax')
fax_input.enter_text("224-422-8196")


address_field = Element(Browser, By.XPATH, "//fieldset/div[2]")
address_field = address_field.get_attribute("class")
assert "required" in address_field
address_input = Element(Browser, By.ID, 'input-address-1')
address_input.enter_text("1048 Emerald dr")


city_field = Element(Browser, By.XPATH, "//fieldset[@id='address']/div[4]")
city_field = city_field.get_attribute("class")
assert "required" in city_field
city_input = Element(Browser, By.ID, 'input-city')
city_input.enter_text("Schaumburg")


password_field = Element(Browser, By.XPATH, "//fieldset/div[1]")
password_field_class = password_field.get_attribute("class")
assert "required" in password_field_class
password_input = Element(Browser, By.ID, "input-password")
password_input.enter_text(15865847)

password_field = Element(Browser, By.XPATH, "//fieldset/div[2]")
password_field_class = password_field.get_attribute("class")
assert "required" in password_field_class
password_input = Element(Browser, By.ID, "input-confirm")
password_input.enter_text("15865847")

# select country
Dropdown(Browser,By.ID, 'input-country').select_by_text("United States")

#find dropdown Element for Country
Dropdown(Browser,By.NAME,'zone_id').select_by_text("Illinois")

# activating My account dropdown
account_btn = driver.find_element_by_xpath("//a[@title='My Account']")
account_btn.click()

# Selecting Register from dropdown

WebDriverWait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']")))
register_option = driver.find_element_by_xpath("//*[@class='dropdown-menu dropdown-menu-right']/li[1]")
register_option.click()

# Selecting Login from dropdown
login_btn = driver.find_element_by_xpath(
    "//a[@name = 'href' and @value ='https://cleveronly.com/brainbucket/index.php?route=account/login']")
login_btn.click()

# subscribe YES radio button
radio_btn = Checkbox(Browser, By.XPATH, "//input[@name= 'newsletter' and @value='1']")
radio_btn.select()

#subscribe to newsletter NO
subscribe_btn_no = driver.find_element_by_xpath("//input[@name= 'newsletter' and @value='0']")
if not subscribe_btn_no.is_selected():
    subscribe_btn_no.click()


# Privacy Policy
checkbox_btn = driver.find_element_by_xpath("//input[@name='agree' @value='1']")
if not checkbox_btn.is_selected():
    checkbox_btn.click()


time.sleep(5)
Browser.shutdown()
