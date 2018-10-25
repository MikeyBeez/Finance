import bs4 as bs
import datetime as dt
import os
import pandas_datareader.data as web
import pickle
import requests
import pandas as pd
import time
import quandl
from pandas import DataFrame

quandl.ApiConfig.api_key = 'UxxaDDVTDhr-56yFDQy2'
quandl.ApiConfig.api_version = '2015-04-09'

def save_sp500_tickers():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)
    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)
    return tickers


# save_sp500_tickers()
def get_data_from_quandl(reload_sp500=False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)
    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    start = dt.datetime(2010, 1, 1)
    end = dt.datetime.now()
    for ticker in tickers:
        # just in case your connection breaks, we'd like to save our progress!
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):


            data = quandl.get_table('WIKI/PRICES', ticker=[ticker],
                                    qopts={'columns': ['date', 'high', 'low', 'open',
                                                       'close', 'volume', 'adj_close']},
                                    date={'gte': '2015-12-31', 'lte': '2016-12-31'},
                                    paginate=True)

            df = DataFrame(data)

            # df = df.drop("Symbol", axis=1)

            df.set_index('date', inplace=True)


            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))


get_data_from_quandl()
