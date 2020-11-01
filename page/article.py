import re


class Article:

    def __init__(self, title, url, description, added, comments):
        self.title = title
        self.url = url
        self.description = description
        self.added = added
        self.comments = comments

    @classmethod
    def create_using_adapter(cls, adapter, title, url, description, added, comments):
        data = adapter.create_article(title, url, description, added, comments)
        return cls(**data)

    def __str__(self):
        return self.url

    def __repr__(self):
        return self.url

    @property
    def id(self) -> int:
        return int(re.findall(r'https:\/\/kanonierzy\.com\/news\/.*\/(\d{4,6})\/', self.url)[0])

    @property
    def url_title(self) -> str:
        return re.findall(r'https:\/\/kanonierzy\.com\/news\/(.*)\/\d{4,6}\/', self.url)[0]

    def show(self):
        from pprint import pprint
        pprint(vars(self))
