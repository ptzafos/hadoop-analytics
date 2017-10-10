import pandas as pd
import datetime

eth = pd.read_csv('ethereum_price.csv')
btc = pd.read_csv('bitcoin_price.csv')
xrp = pd.read_csv('neo_price.csv')
xmr = pd.read_csv('monero_price.csv')
ltc = pd.read_csv('litecoin_price.csv')

result = pd.concat
eth['Date'] = pd.to_datetime(eth['Date'])
btc['Date'] = pd.to_datetime(btc['Date'])
xrp['Date'] = pd.to_datetime(xrp['Date'])
xmr['Date'] = pd.to_datetime(xmr['Date'])
ltc['Date'] = pd.to_datetime(ltc['Date'])
eth.columns = ['eth_' + str(col) for col in eth.columns] 
btc.columns = ['btc_' + str(col) for col in btc.columns] 
xrp.columns = ['xrp_' + str(col) for col in xrp.columns] 
xmr.columns = ['xmr_' + str(col) for col in xmr.columns] 
ltc.columns = ['ltc_' + str(col) for col in ltc.columns] 
result = pd.concat([eth.set_index('eth_Date'),btc.set_index('btc_Date'),xrp.set_index('xrp_Date'),xmr.set_index('xmr_Date'),ltc.set_index('ltc_Date')],axis=1, join='inner')
result.index.names=['Date']
result.to_csv('cryptjoined.csv',encoding='utf8')



