#!/usr/bin/env python

num_friends = [40, 34, 1, 23, 56, 98, 1, 22, 34, 56]

def median(v):
    """ find the 'middle-most' value of v"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        # if odd, return the middle value
        return sorted_v[midpoint]
    else:
        # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

print median(num_friends)   # 6.0
