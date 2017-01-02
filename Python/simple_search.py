#!/usr/bin/env python
# Linear Search

data = [1,2,3,5,6,7]

input_num = raw_input('Enter number to Search :') 

for i in xrange(0, len(data)):
	if data[i] == int(input_num):
		print "Number found at index", i