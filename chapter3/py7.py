#!/usr/bin/env python
# still scatterplot

from matplotlib import pyplot as plt

test_1_grades = [ 99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_1_grades, test_2_grades)
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")
plt.title("Axes aren't comparable")
plt.show()


# we can add plt.axis("equal") to show equal x and y-axis
