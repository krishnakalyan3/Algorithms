#!/usr/bin/env python2
import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
reverse = map(lambda x : str(x), arr[::-1])
print ' '.join(reverse)