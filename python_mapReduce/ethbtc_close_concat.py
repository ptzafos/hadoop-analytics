import pandas as pd
import datetime

eth = pd.read_csv('ethereum_price.csv')
btc = pd.read_csv('bitcoin_price.csv')

ethbtc = pd.concat
eth['Date'] = pd.to_datetime(eth['Date'])
btc['Date'] = pd.to_datetime(btc['Date'])
eth.columns = ['eth_' + str(col) for col in eth.columns] 
btc.columns = ['btc_' + str(col) for col in btc.columns] 
ethbtc = pd.concat([eth.set_index('eth_Date'),btc.set_index('btc_Date')],axis=1, join='inner')
ethbtc.index.names=['Date']
ethbtc.to_csv('ethbtc.csv',header=False,encoding='utf8')



