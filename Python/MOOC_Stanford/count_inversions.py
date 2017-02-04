#!/usr/bin/env python2


def sort(data_array):
	inv  = 0
	for i in range(1,len(data_array)):
		if data_array[i] < data_array[i-1]:
			inv += 1	
	return inv

if __name__ == "__main__":
	data = open("../../data/IntegerArray.txt").read().split('\n')
	print sort(data)
