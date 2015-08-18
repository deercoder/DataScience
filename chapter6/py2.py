#!/usr/bin/env python

# here is some form of PDF and CDF
def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0

# CDF
def uniform_cdf(x):
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1

def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))
