import os
import logging


def _create_log(name):
    path = os.path.join('logs', 'LOGS.log')
    file_handler = logging.FileHandler(path, encoding="utf8")
    formatter = logging.Formatter('%(asctime)s | %(levelname)-5s | %(name)-16s | %(message)s')
    file_handler.setFormatter(formatter)
    log = logging.getLogger(name)
    log.addHandler(file_handler)
    return log


class Logger:
    __instance = None
    logger = None

    def __new__(cls, *args, **kwargs):
        """
        Logger as singleton
        """
        if cls.__instance is None:
            instance = super().__new__(cls, *args, **kwargs)
            cls.__instance = instance
            cls.logger = _create_log("DEBUG")
        return cls.__instance

    @classmethod
    def log(cls, message):
        cls.logger.setLevel(logging.DEBUG)
        cls.logger.debug(message)
