from nomics import Nomics
nomics = Nomics("5d2b06699511813c145b2a982c05f69e")

markets = nomics.Candles.get_candles(interval = '1d', currency = 'BTC')

print(markets)