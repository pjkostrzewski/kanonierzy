from abc import ABC, abstractmethod


class Browser(ABC):
    """ Abstract class for browser engines """

    @abstractmethod
    def get(self, url):
        pass

    @abstractmethod
    def get_cookies(self):
        pass

    @abstractmethod
    def add_cookie(self, cookie):
        pass

    @abstractmethod
    def execute_script(self, script):
        pass

    @abstractmethod
    def find_elements_by_class_name(self, class_name):
        pass

    @abstractmethod
    def add_argument(self, option):
        pass

    @abstractmethod
    def run(self):
        pass
