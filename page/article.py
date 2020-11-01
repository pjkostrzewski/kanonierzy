import re
from datetime import datetime
from dataclasses import dataclass


@dataclass
class Article:
    title: str
    url: str
    description: str
    added: datetime
    comments: int
    picture: str

    @classmethod
    def create_using_adapter(cls, adapter, title, url, description, added, comments, picture):
        data = adapter.create_article(title, url, description, added, comments, picture)
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
