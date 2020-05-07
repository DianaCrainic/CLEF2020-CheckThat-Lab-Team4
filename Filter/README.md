# Team 4' Filtering Task - Structure

1. __filter.py__ - script for tweet filtering (makes use of the [Natural Language Toolkit](https://www.nltk.org/), or __NLTK__ for short):
    * *get_text_from_tweet* - extracts the actual text of the tweet;
    * *tokenizer* - transforms the tweet's text into a list of tokens;
    * *contains_keywords* - checks whether there is a token that appears in the list of keywords from the given file;
    * *contains_tags* - checks whether one of the tweet's tags appears in the list of tags from the given file;
    * *check_for_keywords* - checks if the tweet can be categorized as `news` based on its keywords;
    * *check_for_tags* - checks if the tweet can be categorized as `news` based on its tags;
    * *is_news* - prepares the tweet for verification and returns whether the tweet is `news` or not.
2. __words__ - a directory containing text files with keywords related to different areas:
    * *jobs.txt* - contains keywords related to job advents;
    * *ad.txt* - contains keywords related to ads;
    * *news.txt* - contains keywords related to news;
    * *swear.txt* - contains examples of swears.
3. __tags__ - a directory containing text files with tags related to different areas:
    * *jobs-tags.txt* - contains tags related to job advents;
    * *ad-tags.txt* - contains tags related to ads;
    * *news-tags.txt* - contains tags related to news.

#### All the relevant resources from above were successfully integrated into Team 5's work and the final results can now be further used by the other teams.
