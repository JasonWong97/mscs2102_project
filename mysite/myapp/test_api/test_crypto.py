from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

CRYPTO_API='aeb442d4-d2fd-4703-82d6-0e13ebae0726'
COINS='BTC,ETH,BNB,ADA,USDT'
coin_list=COINS.split(',')

from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError

cmc = CoinMarketCapAPI(CRYPTO_API)

r = cmc.cryptocurrency_quotes_latest(symbol='BTC,ETH,BNB,ADA,USDT')

print(r.data)
print(type(r.data))

coins_latest_info={}
for coin in coin_list:
    coins_latest_info[coin]=r.data[coin]['quote']['USD']['price']

print(coins_latest_info)


