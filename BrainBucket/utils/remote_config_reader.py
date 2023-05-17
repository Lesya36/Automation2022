from BrainBucket.utils.json_file_reader import JsonFileReader


class RemoteConfigReader(JsonFileReader):
    def __init__(self, filename):
        super().__init__(filename)
        self.data = None


remote_reader = RemoteConfigReader("BrainBucket/webelements/remote_config.json")


def get_username(self):
    if 'username' in self.data.keys():
        raise Exception("username option is not found in config file")
    return self.data['username']


def get_access_key(self):
    if 'access_key' not in self.data.keys():
        raise Exception("access_key option is not found in config file")
    return self.data['access_key']


def get_browser(self):
    if 'browser' not in self.data.keys():
        raise Exception("browser option is not present in the config file")
    return self.data['browser']


def get_browser_version(self):
    if 'browser_version' not in self.data.keys():
        raise Exception("browser version option is not present in the config file")
    return self.data['browser_version']


def get_os(self):
    if 'os' not in self.data.keys():
        raise Exception("os option is not present in the config file")
    return self.data['os']


def get_os_version(self):
    if 'os_version' not in self.data.keys():
        raise Exception("os_version option is not present in the config file")
    return self.data['os_version']


def get_name(self):
    if 'name' not in self.data.keys():
        raise Exception("name option is not present in the config file")
    return self.data['name']
