#Exercise #1

class Alert:
    def __init__(self, browser):
        self.alert = browser.get_driver().switch_to.alert

    def accept_alert(self):
        self.alert.accept()

    def dismiss_alert(self):
        self.alert.dismiss()

    def enter_text(self, text):
        self.enter_text(text)
        self.alert.accept()

#Exercise #2


class Iframe:
    def __init__(self, browser):
        self.iframe = browser.get_driver().switch_to.frame

    def switch_to_frame(self):
        self.iframe.switch_to_frame()

    def switch_to_content(self):
        self.iframe.switch_to_content()


