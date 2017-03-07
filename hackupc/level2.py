#!/usr/bin/env python3


if __name__ == '__main__':
	read_data = open("/Users/krishna/Downloads/input.txt").read()
	str_find = read_data.find('1337')
	print(str_find)