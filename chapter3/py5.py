#!/usr/bin/env python

from matplotlib import pyplot as plt

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]

# just pair it like (1, 256), (2, 128)...
# for x, y in zip(variance, bias_squared):
#	print x, y

total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [ i for i, _ in enumerate(variance)] # not list the value, but list the index from 0, ... num-1

## call plot multiple times to draw many series
plt.plot(xs, variance, 'g-', label='variance')	# green color, solid
plt.plot(xs, bias_squared, 'r-.', label='bias^2')	# red color, dot
plt.plot(xs, total_error, 'b:', label='total error')	# blue dotted

# legend will give the blank showing the type of the lines, loc=9 means at the top center shows it
plt.legend(loc=9)

# title and label
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")

# show
plt.show()
