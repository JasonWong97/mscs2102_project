#!/usr/bin/env python

# from nltk.corpus import twitter_samples

# positive_tweets = twitter_samples.strings('positive_tweets.json')
# negative_tweets = twitter_samples.strings('negative_tweets.json')
# text = twitter_samples.strings('tweets.20150430-223406.json')
# tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
# print(tweet_tokens[0][0])

import requests
r = requests.get('https://finnhub.io/api/v1/crypto/exchange?token=c0ja5jn48v6vejle9ntg')
print(r.json())
