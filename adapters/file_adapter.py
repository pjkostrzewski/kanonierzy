import json
import datetime


class FileAdapter:
    def __init__(self, filename="results.json"):
        self.filename = filename

    @staticmethod
    def datetime_converter(something):
        if isinstance(something, datetime.datetime):
            return something.timestamp()

    def save_to_file(self, data):
        with open(self.filename, 'w', encoding="utf-8") as outfile:
            json.dump(data, outfile, default=self.datetime_converter, ensure_ascii=False)

    def append_to_file(self, data):
        with open(self.filename, 'a', encoding="utf-8") as outfile:
            json.dump(data, outfile, default=self.datetime_converter, ensure_ascii=False)

    def read_file(self):
        with open(self.filename, 'r') as json_file:
            data = json.load(json_file)
        return data

