from datetime import datetime
from dataclasses import dataclass


@dataclass
class User:
    user_id: str
    nick: str
    registered: datetime
    added_comments: int
    pluses: int
    last_comment: str
    warnings: int

    @classmethod
    def create_using_adapter(cls, adapter, user_id, nick, registered, added_comments, pluses, last_comment, warnings):
        data = adapter.refactor_data(user_id, nick, registered, added_comments, pluses, last_comment, warnings)
        return cls(**data)

    def __str__(self):
        return self.nick

    def __repr__(self):
        return self.nick

    @property
    def url(self) -> str:
        return f'https://kanonierzy.com/profil/{self.nick}/{self.user_id}/'

    def show(self):
        from pprint import pprint
        pprint(vars(self))

    @property
    def days_since_registration(self):
        diff = datetime.now() - self.registered
        return diff
