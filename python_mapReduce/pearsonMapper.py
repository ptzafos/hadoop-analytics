#!/usr/bin/env python
import sys

SEP = ","


class pearsonMapper(object):

	def __init__(self,stream, sep = SEP):
		self.stream = stream
		self.sep = sep

	def map(self):
		for date,(eth,btc,meth,mbtc) in self:
			ethdiff = eth - meth
			btcdiff = btc - mbtc
			self.emit(date, (str(ethdiff*btcdiff)+self.sep+str(ethdiff**2)+self.sep+str(btcdiff**2)))
			 
	def emit(self,key,value):
		sys.stdout.write("{}{}{}\n".format(key, self.sep,value))

	def __iter__(self):
		for row in self.stream:
			parts = row.split(self.sep)
			try:
				yield parts[0],(float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4]))
			except:
				continue


if __name__ == '__main__':
	
	mapper = pearsonMapper(sys.stdin)
	mapper.map()
