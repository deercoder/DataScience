#!/usr/bin/env python
# generator and iterator

# Generator, iterate but its value is just produced as needed
def lazy_range(n):
	""" a lazy version of range"""
	i = 0
	while i < n:
		yield i
		i += 1


## Second way to generator
lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)

