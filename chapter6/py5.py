#!/usr/bin/env python
""" find the approximate inverse using binary search"""
""" not easy for normal_cdf directly, but can inverse some value by it"""

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0 # normal_cdf(-10) is close to 0
    hi_z, hi_p = 10.0, 1    # normal_cdf(10) is close to 1

    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = (low_p + hi_p) / 2

        if mid_p < p:
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mid_z
