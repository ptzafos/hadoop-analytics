#!/usr/bin/env python

import sys

SEP = ","

class pearsReducer(object):

	def __init__(self, stream, sep = SEP):
		self.stream = stream
		self.sep = sep

	def emit(self, key, value):
		sys.stdout.write("{}{}{}\n".format(key,self.sep,value))

	def __iter__(self):
		for line in self.stream:
			try:
				parts = line.split(self.sep)
				yield parts[0],(float(parts[1]),float(parts[2]))
			except:
				continue	

	def reduce(self):
		
		sn = 0
		seth = 0
		sbtc = 0
		values = list();
		for key, (eth, btc) in self:
			values.append((key,eth,btc))

		for key,eth,btc in values:		
			sn= sn +1
			seth = seth+ eth
			sbtc = sbtc + btc	
			
		meth = seth/sn
		mbtc = sbtc/sn

		for key, eth, btc in values:
			self.emit(key, (str(eth)+self.sep+str(btc)+self.sep+str(meth)+self.sep+str(mbtc)))


if __name__ == '__main__':
	reducer = pearsReducer(sys.stdin);
	reducer.reduce()
