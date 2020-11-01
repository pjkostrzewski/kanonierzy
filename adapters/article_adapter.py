from datetime import datetime


class ArticleAdapter:

    @classmethod
    def create_article(cls, title, url, description, added, comments):
        """
        Refactor dict data from Scraper to Article
        :param data: dict
        :return: dict, refactored data
        """
        added = datetime.strptime(added.strip(), "%d.%m.%Y, %H:%M")
        comments = int(comments.split()[0])
        return dict(title=title, url=url, description=description, added=added, comments=comments)
