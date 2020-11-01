from scrap.kanonierzy_scraper import KanonierzyScraper

from adapters.article_adapter import ArticleAdapter
from page.article import Article
from engine.browser import BrowserChrome


if __name__ == '__main__':
    browser = BrowserChrome()
    browser.add_argument('headless')
    browser.run()
    scraper = KanonierzyScraper(browser)
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
            comments=content_details.find_element_by_class_name("comments").text,
            picture=newsimg.get_attribute("src")
        )
        article = Article.create_using_adapter(adapter=ArticleAdapter, **data)
        all_articles.append(article)

    for article in all_articles:
        article.show()
