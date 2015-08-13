#!/usr/bin/env python
# zip and argument

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zip(list1, list2)	# [('a', 1), ('b', 2), ('c', 3)]

# unzip
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pair)

add(1, 2)	# 3
add([1, 2])	# TypeError
add(*[1, 2])	# 3
