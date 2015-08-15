#!/usr/bin/env python
from matplotlib import pyplot as plt
from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
histogram = [grade//10 * 10 for grade in grades]
counter = Counter(histogram)
print counter

# draw x and y label
plt.xlabel("deciles")
plt.ylabel("# of the Students")

# draw the boundry of the x and y
plt.axis([-5, 105, 0, 5])

# draw the x lables
plt.xticks([x * 10 for x in range(11)])

# draw the bar
plt.bar([x - 4 for x in counter.keys()],
	[x for x in counter.values()],
	8)

# save the figure
plt.savefig("practice-py3.png")

# show it
plt.show()
