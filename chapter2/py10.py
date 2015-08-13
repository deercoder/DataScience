#!/usr/bin/env python
# Trueiness

one_is_less_than_two = 1 < 2		# True
true_equals_false = True == False 	# False

print one_is_less_than_two, true_equals_false

## pythonic code for trueiness
x = None
print x == None	## not pythonic
print x is None

## some code
#	s = some_function_that_returns_a_string()
#	if s:
#		first_char = s[0]
#	else:
#		first_char = ""
###
# Same code that acts more natural:
##	first_char = s and s[0]


## all function that returns truel when ALL are true
print all([True, 1, { 3 }]) # True
print all([True, 1, {}])	# False

# any function: return true when any of the item is true
print any([True, 1, { 3 }])
print all([])
print any([])
