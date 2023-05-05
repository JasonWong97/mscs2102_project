from textblob import TextBlob

import numpy as np
import pandas as pd
a=[
    'RT @LabraFinance: LABRA Introduces AutoStaking. Your $LABRA Balance will automatically go up with every transaction. 1% of every txs get re\xe2\x80\xa6',
    'RT @latitude8848: Day 22 of tweeting @binance until they list #Vertcoin\n\n@Vertcoin @BinanceUS @cz_binance\n\n#cryptotwitter #crypot #cryptocu\xe2\x80\xa6',
    'RT @Seomaster2013: $pnt to Moon Very Soon \xf0\x9f\x98\x89Check @pNetworkDeFi for latest PNT updates. PNT is on  Binance. 30x or more \xf0\x9f\x9a\x80\n\n\xf0\x9f\x92\x9fNFTs to Binance\xe2\x80\xa6',
    '@PeterLBrandt Completely agree that on a month and multi month basis changes in tax policy could have a very large\xe2\x80\xa6 https://t.co/AUOlVC8Kin',
    'RT @AgenorCoin: \xf0\x9f\x94\xa510 AGE ($100)\xf0\x9f\x94\xa5Ends 1st May\n\xf0\x9f\xa4\x96Airdrop Bot \xe2\x80\x94&gt; https://t.co/0lf0sXkX1d\n\xf0\x9f\x94\xb9Join our Telegram group (https://t.co/vLt1kXPG92) \n\xf0\x9f\x94\xb9Fo\xe2\x80\xa6',
    '\xc2\xbfEs #EOS el nuevo #BTC? Presta atenci\xc3\xb3n a lo que dice Peter Thiel\n#bitcoin #Criptomonedas #cryptocurrencies #crypto\nhttps://t.co/ikHH0bUHog',
    '\xf0\x9f\x96\xa4']

dic1 = {'name': a}  # 使用字典进行输入
test_3 = pd.DataFrame(dic1)

# print(test_3)
total_score=0
count=0
for index, row in test_3.iterrows():
    # print(row['name'])
    # print('fdsfs')
    score=TextBlob(row['name']).sentiment.polarity
    if score!=0:
        count+=1
        total_score+=score

avg_score=total_score/count
print(avg_score)
