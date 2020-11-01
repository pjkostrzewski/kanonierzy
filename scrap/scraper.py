from selenium import webdriver
from scrap.config import chromedriver_path
from time import sleep
import pickle
from abc import abstractmethod, ABC


class Scraper(ABC):

    @abstractmethod
    def scrap(self):
        pass

    @staticmethod
    def scroll_down_page(browser, speed=8):
        current_scroll_position, new_height = 0, 1
        while current_scroll_position <= new_height:
            current_scroll_position += speed
            browser.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
            new_height = browser.execute_script("return document.body.scrollHeight")


class KanonierzyScraper(Scraper):
    url = "https://www.kanonierzy.com/"

    def __init__(self, browser_):
        self.browser = browser_
        self.browser.get(self.url)
        cookies = pickle.load(open("kanonierzy_cookies.pkl", "rb"))
        for cookie in cookies:
            self.browser.add_cookie(cookie)
        self.browser.get(self.url)

    def all_news(self):
        return self.browser.find_elements_by_class_name("singlenews")

    def accept_cookies(self):
        return self.browser.find_element_by_css_selector("button")

    def get_cookies(self):
        return self.browser.get_cookies()

    def pickle_dump(self):
        pickle.dump(self.browser.get_cookies(), open("cookies.pkl", "wb"))

    def scrap(self):
        return -1


options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(chromedriver_path, options=options)
scraper = KanonierzyScraper(browser)
sleep(3)
scraper.scroll_down_page(browser)

all_news = scraper.all_news()
for x in all_news:
    # print(x.find_element_by_class_name("newscont").find_element_by_class_name("title").find_element_by_css_selector('a').get_attribute('href'))
    # print(x.find_element_by_class_name("newscont").find_element_by_class_name("title").find_element_by_css_selector('a').get_attribute('text'))
    print(x.find_element_by_class_name("newsimg").get_attribute("src"))
    print(x.find_element_by_class_name("newsimg").get_attribute("alt"))
    print(x.find_element_by_class_name("newscont").find_element_by_class_name("text").find_element_by_css_selector('a').get_attribute('href'))
    print(x.find_element_by_class_name("newscont").find_element_by_class_name("text").find_element_by_class_name("text").text)
    print(x.find_element_by_class_name("newscont").find_element_by_class_name("text").find_element_by_class_name("details").find_element_by_class_name("date").text)
    print(x.find_element_by_class_name("newscont").find_element_by_class_name("text").find_element_by_class_name("details").find_element_by_class_name("comments").text)
    print()
sleep(60)