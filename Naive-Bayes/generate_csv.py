import csv
import json
import sys
import requests
import io
import classifier

TWEET_ID_FIELD = 'id'

TWEET_TEXT_FIELD = 'full_text'
TWEET_RETWEETED_STATUS_FIELD = 'retweeted_status'

TWEET_ENTITIES_FIELD = 'entities'
TWEET_TAGS_FIELD = 'hashtags'
TWEET_TAG_TEXT_FIELD = 'text'

UNLABELED_TWEETS_FILE = "data/unlabeled_tweets.csv"


def get_id(tweet):
    if TWEET_RETWEETED_STATUS_FIELD in tweet:
        return tweet[TWEET_RETWEETED_STATUS_FIELD][TWEET_ID_FIELD]

    return tweet[TWEET_ID_FIELD]


def get_text_from_tweet(tweet):
    if TWEET_RETWEETED_STATUS_FIELD in tweet:
        return tweet[TWEET_RETWEETED_STATUS_FIELD][TWEET_TEXT_FIELD]

    return tweet[TWEET_TEXT_FIELD]


def get_tags(tweet):
    tags_json = tweet[TWEET_ENTITIES_FIELD][TWEET_TAGS_FIELD]
    tags = [tag[TWEET_TAG_TEXT_FIELD] for tag in tags_json]
    return tags


if __name__ == '__main__':
    number_of_tweets = int(sys.argv[1])
    url = "http://ip2020.herokuapp.com/all_unfiltered_tweets/" + str(number_of_tweets)
    json_content = requests.get(url).json()
    tweets = json.loads(json_content)

    list_of_id = []

    with io.open(UNLABELED_TWEETS_FILE, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(number_of_tweets):
            id = get_id(tweets[i])
            if id not in list_of_id:
                list_of_id.append(id)
                text = get_text_from_tweet(tweets[i])
                tags = ' '.join(get_tags(tweets[i]))
                csv_writer.writerow([id, text.replace('\n', ''), tags, " "])
