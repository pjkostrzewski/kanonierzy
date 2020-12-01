from datetime import datetime


class ArticleAdapter:
    """
    Article Adapter class

    changes data format to create Article easily
    """
    @classmethod
    def refactor_data(cls, title, url, description, added, comments, picture) -> dict:
        """
            Refactor dict data from Scraper to Article
        :param title:
        :param url:
        :param description:
        :param added:
        :param comments:
        :param picture:
        :return:
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
