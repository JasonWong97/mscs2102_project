import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = '7SPrh2xcgpxuOLLy13JJfpaMH'
consumer_secret = 'bz1JdRd9BLveGxuWwqAiuo2xwZsoNbByu5vAyl0mvWbJJh6HDS'

access_token = '1360418282755379200-lQ8PIPMT2hh0Z2L9bqjJPZmHwXCwYy'
access_token_secret = 'zcFW0psud0ZWYKe3JG0cwugEZY33rN7bXUsvzNEr5fAOB'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------




t = []
tweets = api.search('BTC', tweet_mode='extended')
for tweet in tweets:
    polarity = TextBlob(tweet.full_text).sentiment.polarity
    subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
    t.append([tweet.full_text,polarity,subjectivity])
    # t.append(tweet.full_text)
print(t)

#---------------------------------------------------------------------------


