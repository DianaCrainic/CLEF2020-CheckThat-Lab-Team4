import json
import requests


def get_url(number_of_tweets):
    return "http://ip2020.herokuapp.com/all/" + str(number_of_tweets)


def get_tweets(url):
    json_content = requests.get(url).json()
    return json.loads(json_content)


def remove_irrelevant_keys(tweets, number_of_tweets, keys_file):
    for i in range(0, number_of_tweets):
        file = open(keys_file)
        for line in file:
            line = line.rstrip()
            tweets[i].pop(line, None)
        file.close()

        user = {'name': tweets[i]['user']['name'], 'location': tweets[i]['user']['location'],
                'verified': tweets[i]['user']['verified'], 'id': tweets[i]['user']['id']}

        tweets[i].pop("user", None)
        tweets[i]['user'] = user

    return tweets


def write_json_to_file(json_content, filename):
    with open(filename, 'w') as outfile:
        json.dump(json_content, outfile)


def main():
    number_of_tweets = 100
    url = get_url(number_of_tweets)
    tweets = get_tweets(url)

    keys_file = "keys.txt"
    tweets = remove_irrelevant_keys(tweets, number_of_tweets, keys_file)

    filename = "data.txt"
    write_json_to_file(tweets, filename)


main()
