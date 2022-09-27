import ccxt
import pandas as pd
from datetime import datetime

def unixTimeConversion(df):
    for index, row in df.iterrows():
        epoch = df.iloc[index,0]
        new_epoch = datetime.fromtimestamp(int(epoch)/1000)
        df.iloc[index,0] = new_epoch
    return df

def getdata(symbol, timeframe, from_datetime, till_datetime, cex, time_offset):
    print(f"{symbol}: {from_datetime}")
        
    if cex == 'Binance':
        exchange = ccxt.binance()
    elif cex == 'Bitstamp':
        exchange = ccxt.bitstamp()

    all_bars = [] 
    from_timestamp = exchange.parse8601(from_datetime)
    if len(till_datetime)>0:
        till_timestamp = exchange.parse8601(till_datetime)
    else:
        till_timestamp = exchange.milliseconds()
    while from_timestamp <= till_timestamp:
        all_bars += exchange.fetch_ohlcv(symbol, timeframe, from_timestamp,None,{'until':till_timestamp})
        from_timestamp = all_bars[-1][0] + time_offset

    df = pd.DataFrame(all_bars, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
    df = unixTimeConversion(df)

    return(df)

def getalldata(symbols, timeframe, from_datetime, till_datetime, cex, time_offset):
    df_dict = {}
    for symbol in symbols:
        df = getdata(symbol, timeframe, from_datetime, till_datetime, cex, time_offset)
        df_dict[symbol] = df

        path = r'./Backtestdata/'
        extension = '.csv'
        tickertag = symbol.replace("/", "")
        path = path + tickertag + extension
        df.to_csv(path, index = True)
    return(df_dict)






