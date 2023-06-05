


# Create Radiobutton/Checkbox class that will be inherited from UIElement class
# and will have a method to select the radio button/checkbox if it's not selected.

# subscribe to newsletter NO
#subscribe_btn_no = driver.find_element_by_xpath("//input[@name= 'newsletter' and @value='0']")

class Checkbox(Element):
    def __init__(self, browser, by, locator):
        super().__init__(browser, by, locator)

    def select(self):
        checkbox_element = self.get_element
        if not checkbox_element.is_selected():
            checkbox_element.click()

    def deselect(self):
        checkbox_element = self.get_element
        if checkbox_element.is_selected():
            checkbox_element.click()

