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
                {'text': 'nsweather'},
                {'text': 'landscape'}]

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
        tweet_text = "The primary way of person-to-person corona virus transmission is via " \
                     "aerosols or small droplets created by breathing, sneezing or coughing. The " \
                     "reach of exhaled air can be effectively reduced using a face mask as shown " \
                     "in the video.coronavirus https://t.co/j4ObME2Te6"

        tokens = word_tokenize(tweet_text.lower())
        # tweet is news
        self.assertEqual(filter.check_for_keywords(tokens), 0)

    def test_news_tweet3(self):
        tweet_text = "MAJOR BREAKING NEWS: NPR Source Says Trump Blocked Coronavirus Testing in January to Aid His" \
                     "Reelection Chances By Keeping US Infection Figures Low NOTE: Please RETWEET this — " \
                     "America needs to know what this monster did. Thousands of future deaths will rightly " \
                     "be laid at his feet."

        tokens = word_tokenize(tweet_text.lower())
        # tweet is news
        self.assertEqual(filter.check_for_keywords(tokens), 0)


    def test_news_tweet4(self):
        tweet_text = "Breaking news story : Scientists have advised people isolating to wear a " \
                     "face mask in doors not to help stop the Covid 19 but to stop you eating too much."

        tokens = word_tokenize(tweet_text.lower())
        # tweet is news
        self.assertEqual(filter.check_for_keywords(tokens), 0)

    # tweet-ul este considerat news intrucat contine cuvantul "news"
    # nu mai trece la verificarile urmatoare, de ex pentru swear words
    def test_news_tweet5(self):
        tweet_text = "You dont think its sad when more people die from the flu every " \
                     "year then from this bullshit your spreading lies about you people in the " \
                     "news are the problem your causing a mass hysteria over nothing you all " \
                     "should be arrested for this madness you all have created."

        tokens = word_tokenize(tweet_text.lower())
        # tweet is not news
        self.assertEqual(filter.check_for_keywords(tokens), 1)

    # desi tweet-ul contine swear word care este cenzurat ("a**h*les"), este considerat ca fiind news
    def test_news_tweet6(self):
        tweet_text = "'Boomers' aren\'t the only a**h*les that would act like that. Not " \
                     "all 'Boomers' are rich enough to have a summer home. Not all 'Boomers' are " \
                     "FOX News fans and Trump supporters. Whitmer would make a much better " \
                     "President than Trump."

        tokens = word_tokenize(tweet_text.lower())
        # tweet is not news
        self.assertEqual(filter.check_for_keywords(tokens), 1)

    def test_news_tweet7(self):
        tweet_text = "Here is the man who always ready to expand his image on the breaking news," \
                     "not only Delhi each n every  political members should know about the " \
                     "situation of of ground label.. Now a days Commitment became complement "

        tokens = word_tokenize(tweet_text.lower())
        # tweet is news
        self.assertEqual(filter.check_for_keywords(tokens), 0)

    def test_news_tweet8(self):
        tweet_text = "Another sad news. Ruth David, a Holocaust survivor and a victim of coronavirus"

        tokens = word_tokenize(tweet_text.lower())
        # tweet is news
        self.assertEqual(filter.check_for_keywords(tokens), 0)

    def test_news_tweet9(self):
        tweet_text = "MAJOR BREAKING NEWS (THE WASHINGTON POST): Trump Privately Proposed Just " \
                     "Letting Coronavirus 'Wash Over' America—Killing Hundreds of Thousands or " \
                     "Millions of Americans But Keeping the Economy Moving"

        tokens = word_tokenize(tweet_text.lower())
        # tweet is news
        self.assertEqual(filter.check_for_keywords(tokens), 0)

    def test_news_tweet10(self):
        tweet_text = "@errjustsaying Stop listen to the news, fully depressing, I think we should " \
                     "do away with is archaic institution, bleeding the British public dry."

        tokens = word_tokenize(tweet_text.lower())
        # tweet is news
        self.assertEqual(filter.check_for_keywords(tokens), 0)

    def test_not_news_tweet1(self):
        tweet_text = "My Easter message. I’m basically the Pope."

        tokens = word_tokenize(tweet_text.lower())
        # tweet is not news
        self.assertEqual(filter.check_for_keywords(tokens), 1)

    def test_not_news_tweet2(self):
        tweet_text = "@FortniteGame Use code Kingo. Happy easter guys ❤"

        tokens = word_tokenize(tweet_text.lower())
        # tweet is not news
        self.assertEqual(filter.check_for_keywords(tokens), 1)

    def test_not_news_tweet3(self):
        tweet_text = "Big Breaking News: The most like BB13 top 4 contest " \
                     "on twitter after BiggBoss over. \n " \
                     "1. #AsimRiaz 48.02 points\n" \
                     "2. #SidharthShukla 25.51 points\n" \
                     "3. #ShehnaazGill 19.48 points\n" \
                     "4. #RashmiDesai 17.58 points\n"

        tokens = word_tokenize(tweet_text.lower())
        # tweet is not news
        self.assertEqual(filter.check_for_keywords(tokens), 1)

    # cuvinte din alta limba - ar fi trebuit sa fie considerat not news
    def test_foreign_words_tweet(self):
        tweet_text = "'รายง่ะ' or 'อาราย'  doesn\'t mean 'what' it's Thai slang use when men or " \
                     "women are shy"

        tokens = word_tokenize(tweet_text.lower())
        # tweet is not news
        self.assertEqual(filter.check_for_keywords(tokens), 1)

    # ar fi trebuit sa fie not news, dar e considerat ca fiind vague
    def test_weather_tweet1(self):
        tweet_text = "Temperature: -5°C Humidity: 72% Windchill: -12°C. Mainly Sunny. Wind: 22 kph"

        tokens = word_tokenize(tweet_text.lower())
        # tweet is not news
        self.assertEqual(filter.check_for_keywords(tokens), 1)

    def test_weather_tweet2(self):
        tweet_text = "Weather report: Sunny and light wind."

        tokens = word_tokenize(tweet_text.lower())
        # tweet is not news
        self.assertEqual(filter.check_for_keywords(tokens), 1)

    def test_weather_tweet3(self):
        tweet_text = "A Winter Weather Advisory has been issued for our listening area from 4:00"

        tokens = word_tokenize(tweet_text.lower())
        # tweet is not news
        self.assertEqual(filter.check_for_keywords(tokens), 1)

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

    def test_covid_tweet1(self):
        tweet_text = "Africans in Guangzhou are on edge, after many are left homeless amid rising xenophobia as China " \
                     "fights a second wave of coronavirus. Many have no recent travel " \
                     "history or known contact with Covid-19 patients."

        tokens = word_tokenize(tweet_text.lower())
        # vague
        self.assertEqual(filter.check_for_keywords(tokens), 2)

    def test_nato_tweet(self):
        tweet_text = "Russia's President Vladimir Putin talks about how the USA, France and UK-led " \
                     "NATO invasion of Libya ruined the country."

        tokens = word_tokenize(tweet_text.lower())
        # vague
        self.assertEqual(filter.check_for_keywords(tokens), 2)

    # tweet de lungime redusa
    def test_covid_tweet2(self):
        tweet_text = "Coronavirus can travel up to 13 feet: study https://t.co/PNxdbr2nqc"

        tokens = word_tokenize(tweet_text.lower())
        # vague
        self.assertEqual(filter.check_for_keywords(tokens), 2)

    # tweet de lungime redusa
    def test_covid_tweet3(self):
        tweet_text = "Grandad, 101, leaves hospital after beating coronavirus https://t.co/eMq1oYG2PL"

        tokens = word_tokenize(tweet_text.lower())
        # vague
        self.assertEqual(filter.check_for_keywords(tokens), 2)

    # tweet de lungime redusa
    def test_easter_tweet(self):
        tweet_text = "Pope Celebrates Joy of Easter Amid Sorrow of Virus, alone "

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
