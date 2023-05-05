# Twitter Streaming with pySpark


# we use the findspark library to locate spark on our local machine
import redis
import findspark

#
findspark.init('/Users/wengjiacheng/spark-3.0.2-bin-hadoop3.2')

# import necessary packages

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import desc

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import functions as F
from textblob import TextBlob
import time

r = redis.StrictRedis(host='localhost', port=6379, db=1)
# we create an instance of SparkContext. we can run this only once since it initiates the entry point and runs
# the operations inside the executors on worker nodes. if you face any issue, just restart the kernel and run it again.
# spark = SparkSession. \
#     builder. \
#     appName("docker_spark_cluster"). \
#     master("spark://localhost:7077"). \
#     config("spark.executor.memory", "512m", ). \
#     config("spark.executor.cores", "1"). \
#     getOrCreate()

spark = SparkSession. \
    builder. \
    appName("local_parallel"). \
    master('local[2]'). \
    getOrCreate()

sc = spark.sparkContext
# sc = SparkContext()

# we initiate the StreamingContext with 10 second batch interval. next we initiate our sqlcontext
ssc = StreamingContext(sc, 1)
sqlContext = SQLContext(sc)

# initiate streaming text from a TCP (socket) source:
socket_stream = ssc.socketTextStream("localhost", 5555)

# lines of tweets with socket_stream window of size 60, or 60 seconds windows of time
lines = socket_stream.window(60)
time.sleep(5)
lines.pprint()

print(type(lines))

# just a tuple to assign names

from collections import namedtuple

fields = ("crypto_c", "sentiment_s")
Tweet = namedtuple('Tweet', fields)


def cleanTweetFunc(tweet_input):
    tweet = tweet_input.replace('http', ' ')
    tweet = tweet.replace('@', ' ')
    tweet = tweet.replace('#', ' ')
    tweet = tweet.replace('RT', ' ')
    tweet = tweet.replace(':', ' ')
    print(tweet)
    print("ssssadasdasda")
    return tweet


# here we apply different operations on the tweets and save them to a temporary sql table

(lines.filter(lambda word: word)  # Checks for hashtag calls
 .map(lambda word: (word.lower(), 1))  # Lower cases the word
 .reduceByKey(lambda a, b: a + b)
 .map(lambda rec: Tweet(rec[0], rec[1]))  # Stores in a Tweet Object
 .foreachRDD(lambda rdd: rdd.toDF().registerTempTable("tweets")))  # Registers only top 10 hashtags to a table.

# .filter(lambda word: word.lower().contains("btc"))  # Checks for hashtag calls

# .reduceByKey(lambda a, b: a + b)
# .map(lambda rec: Tweet('btc', rec[1]))  # Stores in a Tweet Object

# # lines.flatMap(lambda text: text.split( " " ) ).foreachRDD(lambda rdd: rdd.toDF()).registerTempTable("tweets")
# words = lines.select(explode(split(lines.value, "t_end")).alias("word"))
# words = words.na.replace('', None)
# words = words.na.drop()
# words = words.withColumn('word', F.regexp_replace('word', r'http\S+', ''))
# words = words.withColumn('word', F.regexp_replace('word', '@\w+', ''))
# words = words.withColumn('word', F.regexp_replace('word', '#', ''))
# words = words.withColumn('word', F.regexp_replace('word', 'RT', ''))
# words = words.withColumn('word', F.regexp_replace('word', ':', ''))


# from IPython import display
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas

# start streaming and wait couple of minutes to get enought tweets
ssc.start()
time.sleep(5)
count = 0
while count < 100:
    count += 1
    time.sleep(5)
    top_10_tags = sqlContext.sql('Select * from tweets')
    top_10_df = top_10_tags.toPandas()
    print("xsdfgdfg")
    print(top_10_df)
    # display.clear_output(wait=True)
    # plt.figure( figsize = ( 10, 8 ) )
    # sns.barplot( x="count", y="hashtag", data=top_10_df)
    # plt.show()
    btc_count = 0
    btc_total_score = 0
    eth_count = 0
    eth_total_score = 0
    bnb_count = 0
    bnb_total_score = 0
    ada_count = 0
    ada_total_score = 0
    usdt_count = 0
    usdt_total_score = 0

    for index, row in top_10_df.iterrows():
        # print(row['name'])
        # print('fdsfs')
        if row['crypto_c'].find('btc'):
            score = TextBlob(row['crypto_c']).sentiment.polarity
            if score != 0:
                btc_count += 1
                btc_total_score += score
        if row['crypto_c'].find('eth'):
            score = TextBlob(row['crypto_c']).sentiment.polarity
            if score != 0:
                eth_count += 1
                eth_total_score += score
        if row['crypto_c'].find('bnb'):
            score = TextBlob(row['crypto_c']).sentiment.polarity
            if score != 0:
                bnb_count += 1
                bnb_total_score += score
        if row['crypto_c'].find('ada'):
            score = TextBlob(row['crypto_c']).sentiment.polarity
            if score != 0:
                ada_count += 1
                ada_total_score += score
        if row['crypto_c'].find('usdt'):
            score = TextBlob(row['crypto_c']).sentiment.polarity
            if score != 0:
                usdt_count += 1
                usdt_total_score += score

    if btc_count != 0:
        btc_avg_score = btc_total_score / btc_count
    else:
        btc_avg_score = 0

    if eth_count != 0:
        eth_avg_score = eth_total_score / eth_count
    else:
        eth_avg_score = 0

    if bnb_count != 0:
        bnb_avg_score = bnb_total_score / bnb_count
    else:
        bnb_avg_score = 0

    if ada_count != 0:
        ada_avg_score = ada_total_score / ada_count
    else:
        ada_avg_score = 0

    if usdt_count != 0:
        usdt_avg_score = usdt_total_score / usdt_count
    else:
        usdt_avg_score = 0

    print('btc_avg_score')
    print(btc_avg_score)
    print(eth_avg_score)
    print(bnb_avg_score)
    print(ada_avg_score)
    print(usdt_avg_score)

    r.set('btc_avg_score', btc_avg_score)
    r.set('eth_avg_score', eth_avg_score)
    r.set('bnb_avg_score', bnb_avg_score)
    r.set('ada_avg_score', ada_avg_score)
    r.set('usdt_avg_score', usdt_avg_score)

    # print(r.get('foo'))

    # with open('scores.txt','w') as f:
    #     f.write(str(btc_avg_score)+'\n')
    #     f.write(str(eth_avg_score)+'\n')
    #     f.write(str(bnb_avg_score)+'\n')
    #     f.write(str(ada_avg_score)+'\n')
    #     f.write(str(usdt_avg_score)+'\n')

ssc.stop()
