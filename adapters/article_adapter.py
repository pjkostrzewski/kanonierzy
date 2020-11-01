from datetime import datetime


class ArticleAdapter:

    @classmethod
    def refactor_data(cls, title, url, description, added, comments, picture):
        """
        Refactor dict data from Scraper to Article
        :param data: dict
        :return: dict, refactored data
        """
        added = datetime.strptime(added.strip(), "%d.%m.%Y, %H:%M")
        comments = int(comments.split()[0])
        return dict(
            title=title,
            url=url,
            description=description,
            added=added,
            comments=comments,
            picture=picture
        )
