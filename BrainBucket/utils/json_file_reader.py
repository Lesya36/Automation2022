import json


class JsonFileReader:
    def __init__(self, filename):
        self.data = None

        with open(filename, 'r') as config_file:
            self.data = json.load(config_file)

    def get_browser(self):
        if 'browser' not in self.data.keys():
            raise Exception("Browser option is not present in the config file")
        return self.data['browser']

    def get_wait_time(self):
        if 'wait_time' not in self.data.keys():
            raise Exception("Wait_time option is not present in the config file")
        return int(self.data['wait_time'])

    def get_email(self):
        if 'get_email' not in self.data.keys():
            raise Exception("Get_email option is not present in the config file")
        return self.data['get_email']

    def get_password(self, section_name):
        if 'get password' not in self.data.keys():
            raise Exception("Get_password option is not present in the config file")
        return self.data['get password']

    def get_width(self):
        if 'get_width' not in self.data.keys():
            raise Exception("Get_width option is not present in the config file")
        return int(self.data['get_width'])

    def get_length(self):
        if 'get_length' not in self.data.keys():
            raise Exception("Get_length option is not present in the config file")
        return int(self.data['get_length'])

