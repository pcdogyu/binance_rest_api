import requests
import pandas as pd
from datetime import datetime
pd.set_option('expand_frame_repr',False)

def get_single_tickr_data(symbol):
    ticker_url = 'https://api.binance.com/api/v3/ticker/24hr?symbol={}'.format(symbol)
    resp_obj = requests.get(ticker_url)
    json_obj = resp_obj.json()
    fmt_df = pd.DataFrame(json_obj,index=[1])
    # print(json_obj)
    # fmt_df = pd.DataFrame(json_obj,index=[1])   
    # print(fmt_df)
    # col_df = pd.DataFrame(json_obj,index=[0]).columns
    # print(col_df)
    fmt_df['closeTime']= pd.to_datetime(datetime.utcnow())
    # print(fmt_df)
    # print(fmt_df[['symbol','askQty','askPrice','bidPrice', 'bidQty','volume', 'closeTime']])
    print(fmt_df[['symbol','prevClosePrice','closeTime']])
    
    # ticker_df = pd.DataFrame(index=[1], columns=['datetime'] + fmt_df.index.tolist())
    # ticker_df['datetime'] = pd.to_datetime(datetime.utcnow())
    # print(ticker_df)
    # ticker_df[fmt_df.index.tolist()] = fmt_df['1'].values
    
    # return ticker_df
    
    
def pdtest():
    mydataset = {
  'sites': ["Google", "Runoob", "Wiki"],
  'number': [1, 2, 3]}
    myvar = pd.DataFrame(mydataset)
    print(myvar)
def listtest():
    example_list = ['a', 'b', 'c', 'd']
    for i in range(len(example_list)):
        result = example_list[i]
        print(result)

def get_tickers_data(symbols):
    ticker_df = pd.DataFrame()
    # for symbol in symbols
    #     ticker_df = get_single_tickr_data


def main():
    # listtest()
    # symbol_list = ['BTCUSDT','ETHUSDT','BCHUSDT','LTCUSDT']
    # for i in range(len(symbol_list)):
    #     get_single_tickr_data(symbol_list[i])
        
        
    # get_single_tickr_data(symbol)
    # pdtest()
    symbol = ('ETHUSDT')
    get_single_tickr_data(symbol)
    # print(ticker_df)
    
    
if __name__ == '__main__':
    main()