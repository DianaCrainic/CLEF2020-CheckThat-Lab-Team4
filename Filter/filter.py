import json
import pprint
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from autocorrect import Speller

MINIMUM_NUMBER_OF_WORDS = 10
NEWS_KEYWORDS_FILE = "words/news.txt"
SWEAR_KEYWORDS_FILE = "words/swear.txt"
TWEET_TEXT_FIELD = 'full_text'
TWEET_LANGUAGE_FIELD = 'lang'


# tweet - json object
# filename - name of the file which contains irrelevant keys
def remove_irrelevant_keys(tweet):
    with open("words/keys.txt") as keys_file:
        for line in keys_file:
            line = line.rstrip()
            tweet.pop(line, None)

    user = {'name': tweet['user']['name'], 'location': tweet['user']['location'],
            'verified': tweet['user']['verified'], 'id': tweet['user']['id']}

    tweet.pop("user", None)
    tweet['user'] = user

    return tweet


def tokenizer(text):
    tokens = word_tokenize(text)
    return tokens


def remove_stop_words(tokens):
    stop_words = set(stopwords.words('english'))
    filtered_tokens = []

    for word in tokens:
        if word not in stop_words:
            filtered_tokens.append(word)

    return filtered_tokens


def has_spelling_errors(tokens):
    spell = Speller(lang='en')
    for word in tokens:
        if spell(word) != word:
            return True

    return False


def contains_keywords(tokens, filename):
    with open(filename) as keywords_file:
        for line in keywords_file:
            line = line.rstrip()
            for word in tokens:
                if line == word:
                    return True

    return False


def is_news(tweet):
    # written in english
    if tweet[TWEET_LANGUAGE_FIELD] != 'en':
        return False

    tokens = tokenizer(tweet[TWEET_TEXT_FIELD].lower())

    # has at least MINIMUM_NUMBER_OF_WORDS words
    if len(tokens) < MINIMUM_NUMBER_OF_WORDS:
        return False

    # optimisation
    filtered_tokens = remove_stop_words(tokens)

    # check for spelling errors
    # if has_spelling_errors(filtered_tokens):
    #     return False

    # check for news keywords
    if contains_keywords(filtered_tokens, NEWS_KEYWORDS_FILE) is True:
        return True

    # check for swears keywords
    if contains_keywords(filtered_tokens, SWEAR_KEYWORDS_FILE) is True:
        return False

    return True


def test():
    with open("data.txt") as json_file:
        tweets = json.load(json_file)
        for i in range(0, 100):
            if "retweeted_status" in tweets[i]:
                pprint.pprint(tweets[i]["retweeted_status"]["full_text"])
            else:
                pprint.pprint(tweets[i]["full_text"])
            print(is_news(tweets[i]))
            print("--------------------")


test()
