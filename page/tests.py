import unittest
from .article import Article


class LoggerTests(unittest.TestCase):

    def test_id_is_correct(self):
        article = Article(title="Wenger: Mogłem ponownie sprowadzić Anelkę",
                          url="https://kanonierzy.com/news/wenger-moglem-ponownie-sprowadzic-anelke/50631/",
                          description="Arsene Wenger przyznał, iż stanął przed okazją ponownego sprowadzenia Nicolasa Anelki w 2008 roku.",
                          added=None,
                          comments=59)
        self.assertEqual(article.id, 50631)

    def test_url_title_is_correct(self):
        article = Article(title="Wenger: Mogłem ponownie sprowadzić Anelkę",
                          url="https://kanonierzy.com/news/wenger-moglem-ponownie-sprowadzic-anelke/50631/",
                          description="Arsene Wenger przyznał, iż stanął przed okazją ponownego sprowadzenia Nicolasa Anelki w 2008 roku.",
                          added=None,
                          comments=59)
        self.assertEqual(article.url_title, "wenger-moglem-ponownie-sprowadzic-anelke")


if __name__ == '__main__':
    unittest.main()
