# import needed libraries
import quandl
import pandas as pd
from pandas import DataFrame

# add quandl API key for unrestricted
quandl.ApiConfig.api_key = 'UxxaDDVTDhr-56yFDQy2'
# quandl.read_key()
quandl.ApiConfig.api_version = '2015-04-09'
# quandl.save_key("quandabout")
# print(quandl.ApiConfig.api_key)

data = quandl.get_table('WIKI/PRICES', ticker=['AAPL'],
                      qopts={'columns': ['date', 'high', 'low', 'open',
                                         'close', 'volume', 'adj_close']},
                      date={'gte': '2015-12-31', 'lte': '2016-12-31'},
                      paginate=True)

df = DataFrame(data)

#df.reset_index(inplace=True, drop=[0])

df.set_index('date', inplace=True)



print(df)
