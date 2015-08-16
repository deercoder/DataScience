#!/usr/bin/env python
# dispersion
import math

# calculate the range between min and max
def data_range(x):
    return max(x) - min(x)

print data_range(num_friends)

##  after that, the mean is zero for all these dataset
def de_mean(x):
    """ Translate x by substracting its mean, so that result has mean 0"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

# this variance also measures the dispersion
def variance(x):
    """ assumes x has at least two elements"""
    n = len(x)
    deviation = de_mean(x)
    return sum_of_squares(deviation) / (n - 1)

print variance(num_friends)


def standard_deviation(x):
    return math.sqrt(variance(x))


# NOTE:
# the deviation is 1/(n-1) * (\sum{(x_i - x) ** 2})
