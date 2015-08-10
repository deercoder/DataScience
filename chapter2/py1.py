#!/usr/bin/env python
# Python Basic algorithmetic
for i in [1, 2, 3, 4, 5]:
	print i
	for j in [1, 2, 3, 4, 5]:
		print j
		print i + j
	print i
print "done looping"

# not a good writing style
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# good style
easier_to_read_list_of_lists = [ [1, 2, 3],
				 [4, 5, 6],
				 [7, 8, 9] ]

print list_of_lists
print easier_to_read_list_of_lists

