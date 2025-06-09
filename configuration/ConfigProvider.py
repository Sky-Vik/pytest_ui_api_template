import configparser

global_config = configparser.ConfigParser()
global_config.read("test_config.ini")


class ConfigProvider:
    """
    Класс настройки конфигурации проекта
    """
    def __init__(self):
        self.config = global_config

    # можно делать общие методы
    def get(self, section: str, prop: str):
        return self.config[section].get(prop)

    def getint(self, section: str, prop: int):
        return self.config[section].getint(prop)

    # можно делать общие методы
    def get_ui_url(self):
        return self.config["ui"].get("base_url")
