#!/usr/bin/env python

import math
import sys

SEP = ","

class PearsonReducer(object):
	

	def __init__(self, stream, sep = SEP):
		self.stream = stream
		self.sep = sep

	def __iter__(self):
		for line in self.stream:
			try:
				parts = line.split(self.sep)
				yield parts[0], (float(parts[1]), float(parts[2]), float(parts[3]))
			except:
				continue

	def emit(self, key, value):
		sys.stdout.write("{}{}{}\n".format(key,self.sep,value))	


	def reduce(self):
		sethdiff = 0
		sbtcdiff = 0		
		sethbtcdiff = 0
		for key, (ethbtcdiff, ethdiff, btcdiff) in self:
			sethdiff = sethdiff + ethdiff
			sbtcdiff = sbtcdiff + btcdiff
			sethbtcdiff = sethbtcdiff + ethbtcdiff
			r = sethbtcdiff / (math.sqrt(sethdiff) * math.sqrt(sbtcdiff))
			self.emit(key, r)

			
if __name__ == '__main__':
	reducer = PearsonReducer(sys.stdin)
	reducer.reduce()
