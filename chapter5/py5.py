#!/usr/bin/env python
# mode function
from collections import Counter

num_friends = [12, 3, 4, 43, 56, 87, 101, 34, 1111]

def mode(x):
    """ returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems()
            if count == max_count]

print mode(num_friends)
