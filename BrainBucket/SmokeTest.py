from selenium import webdriver
from selenium.webdriver.support.color import Color

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()

logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

newregistratbtn = driver.find_element_by_xpath("//a[contains(text(), 'Continue')]")

background_color = newregistratbtn.value_of_css_property("background-color")
converted_background_color = Color.from_string(background_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'
newregistratbtn.click()

firstname_field = driver.find_element_by_xpath("//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class
firstname_input = driver.find_element_by_id("input-firstname")
firstname_input.clear()
firstname_input.send_keys("Lesya")


lastname_field = driver.find_element_by_xpath("//fieldset/div[3]")
lastname_field_class = lastname_field.get_attribute("class")
assert "required" in lastname_field_class
lastname_input = driver.find_element_by_id("input-lastname")
lastname_input.clear()
lastname_input.send_keys("Khmelovska")


email_field = driver.find_element_by_xpath("//fieldset/div[4]")
email_field_class = email_field.get_attribute("class")
assert "required" in email_field_class
email_input = driver.find_element_by_id("input-email")
email_input.clear()
email_input.send_keys("lesyak1group@gmail.com")


telephone_field = driver.find_element_by_xpath("//fieldset/div[5]")
telephone_field_class = telephone_field.get_attribute("class")
assert "required" in telephone_field_class
telephone_input = driver.find_element_by_id("input-telephone")
telephone_input.clear()
telephone_input.send_keys("224-422-8196")


fax_field = driver.find_element_by_xpath("//fieldset/div[6]")
fax_field_class = fax_field.get_attribute("class")
assert "required" not in fax_field_class
fax_input = driver.find_element_by_id('input-fax')
fax_input.clear()
fax_input.send_keys("224-422-8196")


address_field = driver.find_element_by_xpath("//fieldset/div[2]")
address_field = address_field.get_attribute("class")
assert "required" in address_field
address_input = driver.find_element_by_id('input-address-1')
address_input.clear()
address_input.send_keys("1048 Emerald dr")



city_field = driver.find_element_by_xpath("//fieldset[@id='address']/div[4]")
city_field = city_field.get_attribute("class")
assert "required" in city_field
city_input = driver.find_element_by_id('input-city')
city_input.clear()
city_input.send_keys("Schaumburg")


password_field = driver.find_element_by_xpath("//fieldset/div[1]")
password_field_class = password_field.get_attribute("class")
assert "required" in password_field_class
password_input = driver.find_element_by_id("input-password")
password_input.clear()
password_input.send_keys(15865847)


passwordcnfrm_field = driver.find_element_by_xpath("//fieldset/div[2]")
passwordcnfrm_field_class = passwordcnfrm_field.get_attribute("class")
assert "required" in passwordcnfrm_field_class
passwordcnfrm_input = driver.find_element_by_id("input-confirm")
passwordcnfrm_input.clear()
passwordcnfrm_input.send_keys("15865847")









