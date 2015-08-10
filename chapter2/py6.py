#!/usr/bin/env python
# Tuple (Cannot change value)
my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3	# ---> [1, 3]

try:
	my_tuple[1] = 3
except	TypeError:
	print "cannot modify a tuple"

def sum_and_product(x, y):
	return (x+y),(x*y)

sp = sum_and_product(2, 3)
print sp
s, p = sum_and_product(5, 10)
print s, p

# multiple assignment
x,y = 1,2 # x = 1, y = 2
x,y = y,x # swap them, x = 2, y = 1
