#!/usr/bin/env python3

from joblib import Parallel, delayed
import multiprocessing

input_1 = range(100)
def process(i):
	return i*i

num_cores = multiprocessing.cpu_count()
result = Parallel(n_jobs=4)(delayed(process)(i) for i in input_1)
print(result)