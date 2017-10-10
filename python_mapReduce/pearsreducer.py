#!/usr/bin/env python

import sys
from itertools import groupby
from operator import itemgetter

sep = ","

class pearsReducer(object):

	def __init__(self, stream, sep = SEP):
		self.stream = stream
		self.sep = sep

	def emit(self, key, value):
		sys.stdout.write("{}{}{}\n".format(key,self.sep,value))

	
	def reduce(self):
		sn, seth, sbtc = 0
		for key, eth, btc in self:
			sn = sn+1
			seth = seth+eth
			sbtc = sbtc+btc

		meth = seth/sn
		mbtc = sbtc/sn

		for key, eth, btc in self:
			self.emit(key, (str(eth)+sel.sep+str(btc)+self.sep+str(meth)+self.sep+str(mbtc))

	def __iter__(self):
		for line in self.stream:
		#reader = csv.reader(self.stream)
		#for line in reader:
			try:
				parts = line.split(self.sep)
				yield parts[0],float(parts[1]),float(parts[2])
			except:	
				continue	


if __name__ =='__main__':
	reducer = pearsReducer(sys.stdin);
	reducer.reduce()
