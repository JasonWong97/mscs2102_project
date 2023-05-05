import datetime
from bitdataset import BitDatasetAPI, BitDatasetPandas
import pandas as pd
from datetime import date
# api = BitDatasetAPI('a4c7f4f4-6506-451a-b35c-631e7a2949b9')
# connector = BitDatasetPandas(api)


# Historical quotes
today=date.today()
start_date = (today-datetime.timedelta(days=93)).isoformat()
#
# ohlcv_historical = api.ohlcv_historical_data('bitfinex:BTCUSD', {'period': 'D1', 'start': start_date, 'limit':99})
# for ohlcv in ohlcv_historical:
#     print(ohlcv)
#
# print(type(ohlcv_historical))

# df=pd.DataFrame(ohlcv_historical,columns=['time','open','high','low','close','volume'])
# df.to_csv("t2.csv",index=False)

#
#
# quotes_latest_data= api.quotes_latest_data('okex:BTCUSDT', {'limit':5})
# for quote in quotes_latest_data:
#     print(quote)
import time

millis = int(round(time.time() * 1000))
print(millis)
print(millis-90*24*60*60*1000)
start_date_millis=millis-90*24*60*60*1000
str_start_date_millis=str(start_date_millis)
import requests
url = 'http://api.bitdataset.com/v1/ohlcv/history/BITFINEX:BTCUSD?period=d1&start='+str_start_date_millis+'&limit=99'
headers = {'apikey' : 'a4c7f4f4-6506-451a-b35c-631e7a2949b9'}
response = requests.get(url, headers=headers)
print(response.text)




