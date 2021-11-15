import os
import pandas as pd

from binance.client import Client

client = Client(os.environ['BINANCE_API_KEY'], os.environ['BINANCE_SECRET_KEY'])

tickers = client.get_orderbook_tickers()
#print(tickers)


orderbook = client.get_order_book(symbol="ETHUSDT")
#print(orderbook)

pd_orderbook = pd.DataFrame(orderbook)
print(pd_orderbook)

pd_bids = pd_orderbook['bids']
print(pd_bids)
