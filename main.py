from scrap.kanonierzy_scraper import KanonierzyScraper

from adapters.article_adapter import ArticleAdapter
from page.article import Article
from engine.chrome_browser import BrowserChrome
from adapters.file_adapter import FileAdapter


FILENAME = "results.json"


def get_articles_from_website():
    browser = BrowserChrome()
    browser.add_argument('headless').run()
    scraper = KanonierzyScraper(browser)
    scraper.scroll_down_page(browser)
    return [Article.create_using_adapter(adapter=ArticleAdapter, **data) for data in scraper.scrap()]


def save_articles(articles):
    file_adapter = FileAdapter(filename=FILENAME)
    results = {}
    for idx, x in enumerate([vars(article) for article in articles], start=1):
        results[idx] = x
    file_adapter.save(results)


if __name__ == '__main__':
    articles = get_articles_from_website()
    save_articles(articles)
