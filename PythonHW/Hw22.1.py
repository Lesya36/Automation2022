from selenium.webdriver.common.action_chains import ActionChains
from BrainBucket.webelements.browser import Browser
from BrainBucket.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By
from BrainBucket.webelements.actions import Actions
from selenium.webdriver.common.keys import Keys

"Double click (verify that the background color is changed after performing double click)"

browser = Browser('https://cleveronly.com/practice/')
driver = browser.get_driver()

#get element
double_click = Element(browser, By.XPATH, '//*[@id="card"]/p')
#create action chain object
action = Actions(browser)
#click
action.double_click(double_click)
#color change
background_color = Element(browser, By.ID, 'card').get_attribute('style')
assert background_color == 'background-color: rgb(255,179,128);'


"Press enter in the input field "
"(verify that the message #You pressed the key!# is displayed after you perform the action)"


enter_text = Element(browser, By.XPATH,'//*[@id="key_practice"]/input')
text = Element(browser, By.XPATH, '//*[@id="key_practice"]/p')
action = Actions(browser)
action.send_keys_to_element(enter_text, Keys.ENTER)
print(text.get_text())
assert text.get_text() == "You pressed the key!"


#Open Context menu and select all available options from it:
#Change color (verify that the background color is changed for the box)
#Change font (verify that the text in the box becomes bold after it)
#* Open CleverOnly
#Closing Context Menu by sending ESC Key to the page

context_menu = Element(browser, By.XPATH, '//*[@id="context menu"]/p')
box = Element(browser, By.XPATH, '//div[@id="context_menu"]')
action = Actions(browser)
action.right_click(box)
change_color = Element(browser,By.XPATH, "//li[contains(text(),'Change Color')]")
change_color.click()
assert box.get_css_property("background-color") == "rgb(204, 255, 245,1)"














