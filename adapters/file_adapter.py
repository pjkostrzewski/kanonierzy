import json
import datetime


class FileAdapter:
    encoding = "utf-8"

    def __init__(self, filename="results.json"):
        self.filename = filename

    @staticmethod
    def datetime_converter(something):
        if isinstance(something, datetime.datetime):
            return something.timestamp()

    def save(self, data):
        self._save_to_file(data=data, mode='w')

    def append(self, data):
        self._save_to_file(data=data, mode='a')

    def read_file(self):
        with open(self.filename, 'r') as json_file:
            data = json.load(json_file)
            return data

    def _save_to_file(self, data, mode='w'):
        with open(self.filename, mode, encoding=self.encoding) as outfile:
            json.dump(data, outfile, default=self.datetime_converter, ensure_ascii=False)