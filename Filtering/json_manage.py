import json
import pprint


def print_tweets(tweets, number_of_tweets):
    for i in range(0, number_of_tweets):
        pprint.pprint(tweets[i])
        print("\n-----------------------\n")


def print_text_from_tweets(tweets, number_of_tweets):
    for i in range(0, number_of_tweets):
        print(i)
        if "retweeted_status" in tweets[i]:
            pprint.pprint(tweets[i]["retweeted_status"]["full_text"])
        else:
            pprint.pprint(tweets[i]["full_text"])
        print("\n-----------------------\n")


def get_tweets(filename):
    with open(filename) as json_file:
        tweets = json.load(json_file)
        return tweets


def update_json(json_content, filename):
    with open(filename, 'w') as outfile:
        json.dump(json_content, outfile)


def set_news(tweets, tweet_number, is_news, filename):
    tweets[tweet_number]['news'] = is_news
    update_json(tweets, filename)


def main():
    number_of_tweets = 100
    filename = 'data.txt'
    tweets = get_tweets(filename)
    print_text_from_tweets(tweets, number_of_tweets)
    #print_tweets(tweets, number_of_tweets)


if __name__ == "__main__":
    main()
