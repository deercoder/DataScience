#!/usr/bin/env python
# List comprehension, change from one list to another
even_number = [x for x in range(5) if x % 2 == 0]
print even_number

squares = [x * x for x in range(5)]
print squares

even_squares = [x * x for x in even_number]
print even_squares

# turn a list into dict or set
square_dict = { x: x * x for x in range(5) }
square_set = { x * x for x in [1, -1] } # only 1, as equal
print square_dict
print square_set

# not need the value from list, use `_` to reprsent
zeros = [0 for _ in even_number]
print zeros

# multiple for in a list comprehension
pair = [(x, y) for x in range(10) for y in range(10)]
print pair

# later for can use previous for
increasing_pairs = [(x, y) for x in range(10) for y in range(x+1, 10)]
print increasing_pairs
