#!/usr/bin/env python

import sys
import csv 

SEP = ","

class VariablePairsMapper(object):

        def __init__(self, stream, sep = SEP):
                self.stream = stream
                self.sep = sep

        def emit(self,key,value):
		sys.stdout.write("{}{}{}\n".format(key, self.sep, value))

        def map(self):
		for row in self:
			self.emit(row[0], row[4] + SEP + row[10])

	def __iter__(self):
		reader = csv.reader(self.stream)
		for row in reader:
			yield row

if __name__ == '__main__':

	mapper = VariablePairsMapper(sys.stdin)
	mapper.map()
