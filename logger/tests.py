import unittest
import os
from .logger import Logger


class LoggerTests(unittest.TestCase):

    def test_is_singleton(self):
        logger = Logger()
        logger2 = Logger()
        self.assertEqual(id(logger), id(logger2))

    def test_directory_exists(self):
        Logger()
        path = os.path.join('logs', 'LOGS.log')
        exists = os.path.exists(path)
        self.assertTrue(exists)

    def test_directory_is_dir(self):
        Logger()
        path = os.path.join('logs')
        is_dir = os.path.isdir(path)
        self.assertTrue(is_dir)


if __name__ == '__main__':
    unittest.main()
