# import bs4 as bs
# import datetime as dt
# import os
# import pandas_datareader.data as web
# import requests
import pandas as pd
import pickle


def compile_data():
    with open("sp500tickers.pickle", "rb") as f:
        tickers = pickle.load(f)

    main_df = pd.DataFrame()
    # print(main_df)

    for count, ticker in enumerate(tickers):
        df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
        df.set_index('date', inplace=True)

        df.rename(columns={'adj_close': ticker}, inplace=True)
        df.drop(['open', 'high', 'low', 'close', 'volume'], 1, inplace=True)
        # print(df)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')

        if count % 10 == 0:
            print(count)
    print(main_df.head())
    main_df.to_csv('sp500_joined_closes.csv')


compile_data()