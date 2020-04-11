import unittest
import filter
from nltk.tokenize import word_tokenize


class TestTags(unittest.TestCase):
    def test_news_tags1(self):
        tags = [{'text': 'breakingnews'},
                {'text': 'news'},
                {'text': 'Latestnews'},
                {'text': 'newsupdate'}]

        # tweet is news
        self.assertEqual(filter.check_for_tags(tags), 0)

    def test_news_tags2(self):
        tags = [{'text': 'trendingnews'},
                {'text': 'newspaper'},
                {'text': 'instanews'},
                {'text': 'headlines'}]

        # tweet is news
        self.assertEqual(filter.check_for_tags(tags), 0)

    def test_weather_tags(self):
        tags = [{'text': 'weather'},
                {'text': 'weatherforcast'},
                {'text': 'nsweather'}]

        # tweet is not news
        self.assertEqual(filter.check_for_tags(tags), 1)

    def test_empty_tags(self):
        tags = []

        # tweet is not news
        self.assertEqual(filter.check_for_tags(tags), 2)


class TestKeywords(unittest.TestCase):
    def test_covid_tweet(self):
        tweet_text = "Africans in Guangzhou are on edge, after many are left homeless amid rising xenophobia as China" \
                     " fights a second wave of coronavirus. Many have no recent travel" \
                     " history or known contact with Covid-19 patients."

        tokens = word_tokenize(tweet_text.lower())
        # vague
        self.assertEqual(filter.check_for_keywords(tokens), 2)


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestTags))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestKeywords))

    return suite


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
