import requests
import pandas as pd
from datetime import datetime

def get_single_tickr_data(symbol):
    ticker_url = 'https://api.binance.com/api/v3/ticker/24hr?symbol={}'.format(symbol)
    resp_obj = requests.get(ticker_url)
    json_obj = resp_obj.json()
    # print(json_obj)
    fmt_df = pd.DataFrame(json_obj,index=[1])   
    col_df = pd.DataFrame(json_obj,index=[0]).columns
    # print(col_df)
    fmt_df['closeTime']= pd.to_datetime(datetime.utcnow())
    # print(fmt_df)
    print(fmt_df[['symbol','askQty','askPrice','bidPrice', 'bidQty','volume', 'closeTime']])
    
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

def main():
    # listtest()
    symbol_list = ['BTCUSDT','ETHUSDT','BCHUSDT','LTCUSDT']
    for i in range(len(symbol_list)):
        get_single_tickr_data(symbol_list[i])
        
        
    # get_single_tickr_data(symbol)
    # pdtest()
if __name__ == '__main__':
    main()