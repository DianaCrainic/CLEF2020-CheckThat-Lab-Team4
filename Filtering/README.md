# Team 4's Filtering Task - So Far

1. __keys.txt__ - file to store the ignored keys
2. __data.txt__ - file to store only the relevant information regarding a tweet
3. __json_manage.py__ - contains functions for handling json content:
    * *print_tweets* - pretty prints json content
    * *print_text_from_tweets* - prints the text content of the tweets
    * *get_tweets* - get tweets from file
    * *update_json* - dumps content of json in file#
    * *set_news* - add a new key to json, `news`, and gives it a boolean value 
4. __filter.py__ - contains functions for obtaining json from URL, writing json to file and filtering json content:
    * *remove_irrelevant_keys* - removes unnecessary keys from the tweets
    * *get_tweets* - get tweets from a specified URL
    * *write_json_to_file* - dumps json content in given file
