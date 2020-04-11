import unittest
import filter
from nltk.tokenize import word_tokenize


class TestTags(unittest.TestCase):
    def test_news_tags1(self):
        tags = [{'text': 'breakingnews'},
                {'text': 'news'},
                {'text': 'Latestnews'},
                {'text': 'newsupdate'},
                {'text': 'breaking'}]

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

    def test_jobs_tags(self):
        tags = [{'text': 'newjob'}]

        # tweet is not news
        self.assertEqual(filter.check_for_tags(tags), 1)

    def test_sales_tags(self):
        tags = [{'text': 'ad'}]

        # tweet is not news
        self.assertEqual(filter.check_for_tags(tags), 1)

    def test_empty_tags(self):
        tags = []

        # tweet is not news
        self.assertEqual(filter.check_for_tags(tags), 2)


class TestKeywords(unittest.TestCase):
    def test_news_tweet1(self):
        tweet_text = "BREAKING NEWS: NYC school buildings to remain closed for rest of year, de Blasio announces."

        tokens = word_tokenize(tweet_text.lower())
        # tweet is news
        self.assertEqual(filter.check_for_keywords(tokens), 0)

    def test_news_tweet2(self):
        tweet_text = "MAJOR BREAKING NEWS: NPR Source Says Trump Blocked Coronavirus Testing in January to Aid His"\
                     "Reelection Chances By Keeping US Infection Figures Low NOTE: Please RETWEET this — "\
                     "America needs to know what this monster did. Thousands of future deaths will rightly " \
                     "be laid at his feet."

        tokens = word_tokenize(tweet_text.lower())
        # tweet is news
        self.assertEqual(filter.check_for_keywords(tokens), 0)

    def test_news_tweet3(self):
        tweet_text = "BREAKING NEWS: Manchester United have had their €40M bid for Thomas Partey " \
                     "rejected by Atletico Madrid. However, Manchester United have now increased " \
                     "their bid to €45M which seems to be the most they are willing to offer. If " \
                     "rejected they will seek business elsewhere.\n"

        tokens = word_tokenize(tweet_text.lower())
        # tweet is news
        self.assertEqual(filter.check_for_keywords(tokens), 0)

    def test_news_tweet4(self):
        tweet_text = "Breaking news story : Scientists have advised people isolating to wear a " \
                     "face mask in doors not to help stop the Covid 19 but to stop you eating too much."

        tokens = word_tokenize(tweet_text.lower())
        # tweet is news
        self.assertEqual(filter.check_for_keywords(tokens), 0)

    #!!! a adaugat la swear words si "bullshit", dar contine cuvantul "news" si il ca find news, intrucat
    # nu mai trece la verificarile urmatoare
    def test_news_tweet5(self):
        tweet_text = "You dont think its sad when more people die from the flu every " \
                     "year then from this bullshit your spreading lies about you people in the " \
                     "news are the problem your causing a mass hysteria over nothing you all " \
                     "should be arrested for this madness you all have created."

        tokens = word_tokenize(tweet_text.lower())
        # tweet is news
        self.assertEqual(filter.check_for_keywords(tokens), 0)

    #ar fi trebuit sa fie not news, dar e categorisit ca fiind vague
    def test_weather_tweet1(self):
        tweet_text = "Temperature: -5°C Humidity: 72% Windchill: -12°C. Mainly Sunny. Wind: 22 kph"

        tokens = word_tokenize(tweet_text.lower())
        # tweet is not news
        self.assertEqual(filter.check_for_keywords(tokens), 2)

    def test_weather_tweet2(self):
        tweet_text = "A Winter Weather Advisory has been issued for our listening area from 4:00"

        tokens = word_tokenize(tweet_text.lower())
        # tweet is not news
        self.assertEqual(filter.check_for_keywords(tokens), 2)


    def test_emergency_declaration_tweet(self):
        tweet_text = "Premier Doug Ford extends Ontario's emergency declaration until April 23"

        tokens = word_tokenize(tweet_text.lower())
        # vague
        self.assertEqual(filter.check_for_keywords(tokens), 2)

    def test_crisis_tweet(self):
        tweet_text = "I think we have just got to throw stuff up against " \
                     "the wall and see what sticks, adding there is a risk that otherwise, by the " \
                     "time we have got around to doing this the crisis will be over and we will be " \
                     "back to business as usual."

        tokens = word_tokenize(tweet_text.lower())
        # vague
        self.assertEqual(filter.check_for_keywords(tokens), 2)

    def test_tariff_tweet(self):
        tweet_text = "Eskom announced in a statement on Saturday that the National Energy " \
                     "Regulator of SA (Nersa) had approved tariff increases."

        tokens = word_tokenize(tweet_text.lower())
        # vague
        self.assertEqual(filter.check_for_keywords(tokens), 2)

    def test_covid_tweet(self):
        tweet_text = "Africans in Guangzhou are on edge, after many are left homeless amid rising xenophobia as China " \
                     "fights a second wave of coronavirus. Many have no recent travel " \
                     "history or known contact with Covid-19 patients."

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
