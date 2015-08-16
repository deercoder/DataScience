#!/usr/bin/env python
from collections import Counter
from matplotlib import pyplot as plt

num_friends = [100, 49, 41, 40, 25]

# calculate the count of each of the numbers
friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]

plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])

plt.title("Histogram of Friend Counts")
plt.xlabel("# Of friends")
plt.ylabel("# Of people")

plt.show()
