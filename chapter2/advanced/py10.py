#!/usr/bin/env python # args and kwargs

# return 2 * f(x)
def doubler(f):
	def g(x):
		return 2 * f(x)
	return g

# 
def f1(x):
	return x + 1

g = doubler(f1)
print g(3)	# 8
print g(-1)	# 0


def f2(x, y):
	return x + y

g = doubler(f2)
print g(1, 2)	# error, g() only takes one parameters, line 5


# ----> solution 
def magic(*args, **kwargs):
	print "unnamed args:", args
	print "keyword args:", kwargs

magic(1, 2, key="word", key2="word2")

# prints
# unnamed args: (1, 2)
# keyword args: {'key2':'word2', 'key':'word'}

def other_way_magic(x, y, z):
	return x + y + z

x_y_list = [1, 2]
z_dict = {"z": 3}
print other_way_magic(*x_y_list, **z_dict)	#  6


### deal with multiple parameters
def doubler_correct(f):
	"""works no matter what kind of inputs f expects"""
	def g(*args, **kwargs):
	""" whatever arguments g is supplied"""
		return 2 * f(*args, **kwargs)
	return g

g = doubler_correct(f2)
print g(1, 2)	# 6

