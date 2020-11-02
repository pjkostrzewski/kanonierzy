from scrap.kanonierzy_scraper import KanonierzyScraper

from adapters.article_adapter import ArticleAdapter
from page.article import Article
from engine.chrome_browser import BrowserChrome


if __name__ == '__main__':
    browser = BrowserChrome()
    browser.add_argument('headless')
    browser.run()
    scraper = KanonierzyScraper(browser)
    scraper.scroll_down_page(browser)
    all_articles = [Article.create_using_adapter(adapter=ArticleAdapter, **data) for data in scraper.scrap()]
    for article in all_articles:
        article.show()
