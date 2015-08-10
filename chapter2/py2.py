#!/usr/bin/env python
# Python Function
def double(x):
	"""this is where you put an optional docstring
	that explains what the function does.
	for example, this function multiplies its input by 2"""
	return x * 2


# We can pass function as a variable, and assign variable to call it
def apply_to_one(f):
	"""call the function f with 1 as its argument"""
	return f(1)

my_double = double
x = apply_to_one(my_double)	## pass the function my_double ==> double
print x	# equals to 2, double(1)

y = apply_to_one(lambda x:x+4) ## use a annoymous name as lambda in python, accepts x, f=x+4
print y # calls lambda(1) ---> x+4=5, so output 5

# bad practice
another_double = lambda x: 2 * x	#OK,but bad, another_double is the function 2 * x

# Use like this way
def another_double(x):
	return 2 * x

# default parameter
def my_print(message="my default message"):
	print message

my_print("hello")
my_print()

def substract(a=0, b=0):
	return a - b

print substract(10, 5)
print substract(0, 5)
print substract(b=5)
