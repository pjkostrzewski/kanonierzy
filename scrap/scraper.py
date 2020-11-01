import pickle
from time import sleep
from selenium import webdriver

from scrap.config import chromedriver_path
from page.article import Article
from adapters.article_adapter import ArticleAdapter
from abc import ABC, abstractmethod


class Scraper(ABC):

    url = None

    def __init__(self, browser):
        self.browser = browser

    @abstractmethod
    def scrap(self):
        raise NotImplementedError

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

    def get_website(self):
        self.browser.get(self.url)

    def get_cookies(self):
        return self.browser.get_cookies()

    def pickle_dump(self, filepath=None):
        if filepath is None:
            filepath = "{}.pkl".format(self.__class__.__name__)
        pickle.dump(self.browser.get_cookies(), open(filepath, "wb"))


class KanonierzyScraper(Scraper):

    url = "https://www.kanonierzy.com/"

    def __init__(self, browser):
        super().__init__(browser)
        self.get_website()
    def get_website(self):
        self.browser.get(self.url)
        self.load_cookies_from_file("kanonierzy_cookies.pkl")
        self.browser.get(self.url)

    def scrap(self):
        return self.all_news()

    def all_news(self):
        return self.browser.find_elements_by_class_name("singlenews")


options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(chromedriver_path, options=options)
scraper = KanonierzyScraper(browser)
sleep(3)
scraper.scroll_down_page(browser)

all_news = scraper.all_news()
all_articles = []

for news in all_news:
    newsimg = news.find_element_by_class_name("newsimg")
    content = news.find_element_by_class_name("newscont").find_element_by_class_name("text")
    content_details = content.find_element_by_class_name("details")
    data = dict(
        title=newsimg.get_attribute("alt"),
        url=content.find_element_by_css_selector('a').get_attribute('href'),
        description=content.find_element_by_class_name("text").text,
        added=content_details.find_element_by_class_name("date").text,
        comments=content_details.find_element_by_class_name("comments").text
    )
    article = Article.create_using_adapter(adapter=ArticleAdapter, **data)
    all_articles.append(article)

for article in all_articles:
    article.show()
