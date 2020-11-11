from scrap.kanonierzy_scraper import KanonierzyScraper

from adapters.article_adapter import ArticleAdapter
from page.article import Article
from engine.chrome_browser import BrowserChrome
from adapters.file_adapter import FileAdapter


if __name__ == '__main__':
    browser = BrowserChrome()
    browser.add_argument('headless')
    browser.run()
    scraper = KanonierzyScraper(browser)
    scraper.scroll_down_page(browser)
    all_articles = [Article.create_using_adapter(adapter=ArticleAdapter, **data) for data in scraper.scrap()]
    file_adapter = FileAdapter()
    results = {}
    for idx, x in enumerate([vars(article) for article in all_articles]):
        results[idx] = x
    file_adapter.save_to_file(results)
    # for article in all_articles:
    #     article.show()

