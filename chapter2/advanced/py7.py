#!/usr/bin/env python
# Function tool
from functools.partial

def exp(base, power):
	return base ** power

## use traditonal way, calculate the 2**power
def two_to_one(power):
	return exp(2, power)

two_to_the = partial(exp, 2) # function with one variable
print two_to_the(3)	# 8

# fill later part of the parameter
square_of = partial(exp, power=2)
print square_of(3)	# 9

## other tools

def double(x):
	return 2 * x

xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs]
twice_xs = map(double, xs)	# as the above function
list_doubler = parital(map, double) # function that doubles the value
twice_xs = list_doubler(xs)	# same


## test
def multiply(x, y):
	return x * y

# [1 * 4, 2 * 5] 
products = map(multiply, [1, 2], [4, 5])

# filter
def is_even(x):
	""" True if x is even"""
	return x % 2 == 0
	

x_evens = [x for x in xs if is_even(x)]
x_evens = filter(is_even, xs)	# same as above
list_evener = partial(filter, is_even)
x_evens = list_evener(xs)

# reduce combines
x_product = reduce(multiply, xs)
list_product = partial(reduce, multiply)
x_product = list_product(xs)
