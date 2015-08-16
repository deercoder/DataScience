#!/usr/bin/env python
from collections import Counter
from matplotlib import pyplot as plt

num_friends = [100, 49, 41, 40, 25]

# calculate the count of each of the numbers
friend_counts = Counter(num_friends)

# [1]now get the count of the whole data
num_points = len(num_friends)

# [1]now get the largest and smallest
largest_value = max(num_friends)
smallest_value = min(num_friends)

# [1]sort the number
sorted_values = sorted(num_friends)
smallest_value = sorted_value[0]
second_smallest_value = sorted_value[1]
second_largest_value = sorted_value[-2]
# end of [1], these part of statistic

xs = range(101)
ys = [friend_counts[x] for x in xs]

plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])

plt.title("Histogram of Friend Counts")
plt.xlabel("# Of friends")
plt.ylabel("# Of people")

plt.show()
