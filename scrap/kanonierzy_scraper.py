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

    def scrap(self) -> list:
        all_news = self.browser.find_elements_by_class_name("singlenews")
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
                comments=content_details.find_element_by_class_name("comments").text,
                picture=newsimg.get_attribute("src")
            )
            all_articles.append(data)
        return all_articles
