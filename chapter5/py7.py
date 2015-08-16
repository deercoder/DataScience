#!/usr/bin/env python

# here covariance is the dot product of the two vectors, that value may be postive, negtive, zero(non-related)
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

print covariance(num_firends, dialy_minutes)


# fix the unit problem, that above covariance has unit, if x or y is very large, then it's large, but in fact it
# is not so related, so we need to divide them by stdev_x and stdev_y
# that is as the standard_deviation function
def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)

    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0
