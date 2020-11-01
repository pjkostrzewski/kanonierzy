import pickle

from abc import ABC, abstractmethod


class Scraper(ABC):

    url = None

    def __init__(self, browser):
        self.browser = browser

    @abstractmethod
    def scrap(self):
        raise NotImplementedError

    def get_website(self):
        self.browser.get(self.url)

    def load_cookies_from_file(self, filepath):
        cookies = pickle.load(open(filepath, "rb"))
        for cookie in cookies:
            self.browser.add_cookie(cookie)

    @staticmethod
    def scroll_down_page(browser, speed=8):
        current_scroll_position, new_height = 0, 1
        while current_scroll_position <= new_height:
            current_scroll_position += speed
            browser.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
            new_height = browser.execute_script("return document.body.scrollHeight")

    def get_cookies(self):
        return self.browser.get_cookies()

    def pickle_dump(self, filepath=None):
        if filepath is None:
            filepath = "{}.pkl".format(self.__class__.__name__)
        pickle.dump(self.browser.get_cookies(), open(filepath, "wb"))
