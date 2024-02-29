import configparser

config = configparser.RawConfigParser()
config.read("C:\\Fremework projects\\nopcommerce\\nopcommerce_framework\\Configaration\\config.ini")


class Readconfig:
    @staticmethod
    def getEmail():
        email = config.get('Login data', 'userEmail')
        return email

    @staticmethod
    def getPassword():
        password = config.get("Login data", "password")
        return password
