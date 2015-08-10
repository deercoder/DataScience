#!/usr/bin/env python
# List

# List, a few items, like array in another language
integer_list = [1, 2, 3]
hetergeneous_list = ["string", 0.1, True]
list_of_lists = [ integer_list, hetergeneous_list, [] ]	# can be very different

list_length = len(integer_list)
list_sum = sum(integer_list)
print list_length, list_sum

## Get or Set nth element value using a[] operation
x = range(10)
zero = x[0]
one = x[1]
nine = x[-1]
eight = x[-2]
x[0] = -1	# assign it

## Slice the list
first_three = x[:3]
three_to_end = x[3:]
one_to_four = x[1:5]
last_three = x[-3:]
without_first_and_last = x[1:-1]
copy_of_x = x[:]

## _in_ operator for check membership
print 1 in [1, 2, 3] # prints out True
print 0 in [1, 2, 3] # False

## extend list
x = [1, 2, 3]
x.extend([4, 5, 6]) # will CHANGE x

## not change x
x = [1, 2, 3]
y = x + [4, 5, 6]

## Apend to x
x = [1, 2, 3]
x.append(0)
y = x[-1]
z = len(x)

## unpack the list, get it seprately 
x, y = [1, 2] # x = 1, y = 2, after assignment
_, y = [1, 2] # don't want some value, just use underscore

