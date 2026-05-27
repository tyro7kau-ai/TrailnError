import configparser
import os

config = configparser.RawConfigParser()

# 1. Get the directory where readProperties.py is located (.../utilities)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Step back one folder to the root, then navigate to Configurations/config.ini
config_path = os.path.join(current_dir, '..', 'Configurations', 'config.ini')

# 3. Read the absolute path
config.read(config_path)

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = (config.get('commonInfo', 'email'))
        return username

    @staticmethod
    def getPassword():
        password = (config.get('commonInfo', 'password'))
        return password

# Testing above methods - optional Code
# print(ReadConfig.getApplicationURL())
# print(ReadConfig.getUseremail())
