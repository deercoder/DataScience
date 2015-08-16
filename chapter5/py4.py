#!/usr/bin/env python

num_friends = [12, 33, 22, 111, 43, 222, 21566, 78, 2, 3, 9, 10]

def quantile(x, p):
    """ return the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

print quantile(num_friends, 0.10)
print quantile(num_friends, 0.25)
print quantile(num_friends, 0.75)
print quantile(num_friends, 0.90)
