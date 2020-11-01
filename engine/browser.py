from selenium import webdriver

from scrap.config import chromedriver_path


class BrowserChrome:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        # self.browser = webdriver.Chrome(chromedriver_path, options=options)
        self.browser = None

    def get(self, url):
        return self.browser.get(url)

    def get_cookies(self):
        return self.browser.get_cookies()

    def add_cookie(self, cookie):
        self.browser.add_cookie(cookie)

    def execute_script(self, script):
        return self.browser.execute_script(script)

    def find_elements_by_class_name(self, class_name):
        return self.browser.find_elements_by_class_name(class_name)

    def add_argument(self, option):
        assert option in {"start-maximized", "incognito", "headless",
                          "disable-extensions", "disable-popup-blocking",
                          "make-default-browser", "version", "disable-infobars"}, "Wrong option: {}".format(option)
        self.options.add_argument(option)
        return self

    def run(self):
        self.browser = webdriver.Chrome(chromedriver_path, options=self.options)
