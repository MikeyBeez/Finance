import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import matplotlib.dates as mdates
from mpl_finance import candlestick_ochl

style.use('ggplot')

# start = dt.datetime(2015, 1, 1)
# end = dt.datetime.now()
#
# df = web.DataReader("TSLA", 'yahoo', start, end)
#
# print(df.head())


# df.reset_index(inplace=True)
# df.set_index("Date", inplace=True)
# # df = df.drop("Symbol", axis=1)
#
# print(df.tail())

# df.to_csv('tsla.csv')

df = pd.read_csv('tsla.csv',parse_dates=True, index_col=0)
df_ohlc = df ['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()
df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

print(df_ohlc.head())

# print(df.head())

# df['Adj Close'].plot()
# plt.show()
# print(df.describe())
# df['100ma'] = df['Adj Close'].rolling(window=100).mean()
# df.dropna(inplace=True)
# print(df.tail())
# print(df.head())

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)
ax1.xaxis_date()

print(df_ohlc.values)
candlestick_ochl(ax1, df_ohlc.values, width=5, colorup='g', colordown='r')

ax2.fill_between(df_volume.index.map(mdates.date2num),df_volume.values,0)



# ax1.plot(df.index, df['Adj Close'])
# ax1.plot(df.index, df['100ma'])
# ax2.bar(df.index, df['Volume'])
#
plt.show()
