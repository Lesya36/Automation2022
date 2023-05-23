from BrainBucket.utils.json_file_reader import JsonFileReader


class RemoteConfigReader(JsonFileReader):
    def __init__(self, filename):
        super().__init__(filename)

    def get_username(self):
        if 'username' in self.data.keys():
            raise Exception("username option is not found in config file")
        return self.data['username']

    def get_access_key(self):
        if 'access_key' not in self.data.keys():
            raise Exception("access_key option is not found in config file")
        return self.data['access_key']

    def get_desired_cap(self):
        if 'desired_cap' not in self.data.keys():
            raise Exception("desired_cap option is not present in the config file")
        return self.data['desired_cap']

