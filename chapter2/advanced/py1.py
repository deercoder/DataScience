#!/usr/bin/env python
# sorting

x = [4, 1, 2, 3]
y = sorted(x)	# sort x, but x is unchanged
print y
x.sort()  # now x changes, let's see x
print x

# sort by your sequence order and function
x = sorted([-4, 1, -2, 3], key=abs, reverse=True)
print x

wc = sorted(word_counts.items(),
		key=lambda(word, count): count,
		reverse=True)
