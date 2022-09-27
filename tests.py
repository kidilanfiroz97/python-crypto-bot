import ccxt
import pandas as pd
from datetime import datetime

def unixTimeConversion(df):
    for index, row in df.iterrows():
        epoch = df.iloc[index,0]
        new_epoch = datetime.fromtimestamp(int(epoch)/1000)
        df.iloc[index,0] = new_epoch
    return df
exchange = ccxt.binance()
timeframe = '12h'
time_frames = {
    '1s': 1000,
    '1m': 60 * 1000,
    '3m': 3 * 60 * 1000,
    '5m': 5 * 60 * 1000,
    '15m': 15 * 60 * 1000,
    '30m': 30 * 60 * 1000,
    '1h': 60 * 60 * 1000,
    '2h': 2 * 60 * 60 * 1000,
    '4h': 4 * 60 * 60 * 1000,
    '6h': 6 * 60 * 60 * 1000,
    '8h': 8 * 60 * 60 * 1000,
    '12h': 12 * 60 * 60 * 1000,
    '1d': 24 * 60 * 60 * 1000,
    '3d': 3 * 24 * 60 * 60 * 1000,
    '1w': 7 * 24 * 60 * 60 * 1000,
    '1M': 30 * 24 * 60 * 60 * 1000
}

from_datetime = '2018-01-01 00:00:00'
from_timestamp = exchange.parse8601(from_datetime)
till_datetime = '2020-01-01 00:00:00'

if len(till_datetime)>0:
    till_timestamp = exchange.parse8601(till_datetime)
    print(till_timestamp)
else:
    till_timestamp = exchange.milliseconds()
ohlcvs = []

while from_timestamp <= till_timestamp:
    ohlcvs += exchange.fetch_ohlcv('ETH/BTC', timeframe, from_timestamp,None,{'until':till_timestamp})
    from_timestamp = ohlcvs[-1][0] + time_frames[timeframe]
df = pd.DataFrame(ohlcvs, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
df = unixTimeConversion(df)
print(df)