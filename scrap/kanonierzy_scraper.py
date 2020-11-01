from scrap.scraper import Scraper


class KanonierzyScraper(Scraper):

    url = "https://www.kanonierzy.com/"

    def __init__(self, browser):
        super().__init__(browser)
        self.get_website()

    def get_website(self):
        self.browser.get(self.url)
        self.load_cookies_from_file("scrap/kanonierzy_cookies.pkl")
        self.browser.get(self.url)

    def scrap(self):
        return self.all_news()

    def all_news(self):
        return self.browser.find_elements_by_class_name("singlenews")
