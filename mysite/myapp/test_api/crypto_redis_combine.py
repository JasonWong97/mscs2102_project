from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json



from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
from redis import StrictRedis,Redis,ConnectionPool
import time


CRYPTO_API='aeb442d4-d2fd-4703-82d6-0e13ebae0726'
COINS='BTC,ETH,BNB,ADA,USDT'
coin_list=COINS.split(',')
cmc = CoinMarketCapAPI(CRYPTO_API)

r = cmc.cryptocurrency_quotes_latest(symbol='BTC,ETH,BNB,ADA,USDT')

print(r.data)
print(type(r.data))

coins_latest_info={}
for coin in coin_list:
    coins_latest_info[coin]=r.data[coin]['quote']['USD']['price']

print(coins_latest_info)




t={"query_time":time.time(),"price":coins_latest_info}
pool=ConnectionPool(host='localhost',port=6379,db=0,password=None)
r=Redis(connection_pool=pool)
t_json=json.dumps(t)
r.set("Jason",t_json)
print(r.get('Jason'))
