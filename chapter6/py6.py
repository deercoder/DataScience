#!/usr/bin/env python
from collections import Counter
import random
import matplotlib.pyplot as plt
import math

def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binormial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

## the mean of bernoulli(p) is p, and its standard deviation is sqrt(p(1-p))

# the central limit theorem says that if n gets large, a binomial(n,p) is approximately a normal distribution with mean u = np and standard deviation sigma=sqrt(np(1-p))


def make_hist(p, n, num_points):

    data = [binormial(n,p) for _ in range(num_points)]

    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
            [v / num_points for v in histogram.values()],
            0.8,
            color = '0.75')

    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))
    # use a line chart to show the normal approximation
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i+0.5, mu, sigma) - normal_cdf(i-0.5, mu, sigma)
            for i in xs]

    plt.plot(xs, ys)
    plt.title("Binomial Distribution vs. Normal Approximation")
    plt.show()

make_hist(0.75, 100, 10000)
