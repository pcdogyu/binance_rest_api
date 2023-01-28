import requests
import time
import pandas as pd
from datetime import datetime
pd.set_option('expand_frame_repr',False)

def get_single_tickr_data(symbol):
    ticker_url = 'https://api.binance.com/api/v3/ticker/24hr?symbol={}'.format(symbol)
    resp_obj = requests.get(ticker_url)
    json_obj = resp_obj.json()
    fmt_df = pd.DataFrame(json_obj,index=[0])
    return fmt_df

def get_tickers_data(symbol_list):
    tickers_df = pd.DataFrame()
    for symbol in symbol_list:
        ticker_df = get_single_tickr_data(symbol)
        # tickers_df = tickers_df.append(ticker_df)
        tickers_df = pd.concat([tickers_df,ticker_df],axis=0)
    return tickers_df

def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec

def main():
    symbol_list = ['BTCUSDT','ETHUSDT','BCHUSDT','LTCUSDT','XRPUSDT','XLMUSDT']
    tickers_df = get_tickers_data(symbol_list)
    
    print(tickers_df[['symbol','askQty','askPrice','bidPrice', 'bidQty','volume', 'closeTime']])

    
# if __name__ == '__main__':
#     second = sleeptime (0,0,5)    
#     time.sleep(second)   
#     main()

seconds = sleeptime (0,0,5)
while 1 == 1:
    time.sleep(seconds)
    main()
    
    print(datetime.now())
    print("wait for 5 second")
    