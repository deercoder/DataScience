#!/usr/bin/env python
from matplotlib import pyplot as plt
from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)
print histogram # {80: 4, 70: 3, 0: 2, 90: 2, 100: 1, 60: 1}

# as above shows, decile is used for getting decile part, because first
# it get the decimal number, then multiple by 10
# ************** Code below ******************
# for grade in grades:
#	print decile(grade) # get the decile part,

plt.bar([x - 4 for x in histogram.keys()],  # shift to left by 4
	histogram.values(),	# value, which is height 
	8)	# width of the bar
plt.axis([-5, 105, 0, 5])	# x from -5 to 105, y from 0 to 5

plt.xticks([10 * i for i in range(11)])	# label at 0, 10, ..., 100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.savefig("py3.png")
plt.show()


# bar() accepts the key, value(which is x value and y value...), and it
# also accepts the width of the bar
#
# xticks() accepts the label of the x axis that will show on x-axis
#
# axis() sets the range/boundry of the x and y axis

