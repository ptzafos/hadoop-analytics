import pandas as pd
import datetime
import sys

if(len(sys.argv)<2):
	print "You need at least two arguments"
	sys.exit

eth = pd.read_csv(sys.argv[1])
btc = pd.read_csv(sys.argv[2])

ethbtc = pd.concat
eth['Date'] = pd.to_datetime(eth['Date'])
btc['Date'] = pd.to_datetime(btc['Date'])
eth.columns = ['eth_' + str(col) for col in eth.columns] 
btc.columns = ['btc_' + str(col) for col in btc.columns] 
ethbtc = pd.concat([eth.set_index('eth_Date'),btc.set_index('btc_Date')],axis=1, join='inner')
ethbtc.index.names=['Date']
ethbtc.sort_index(inplace=True)
ethbtc.to_csv('ethbtc.csv',header=False,encoding='utf8')



