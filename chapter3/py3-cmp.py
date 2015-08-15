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

plt.bar([x for x in histogram.keys()],  # shift to left by 4
	histogram.values(),	# value, which is height 
	8)	# width of the bar
plt.axis([0, 100, 0, 5])	# x from -5 to 105, y from 0 to 5

plt.xticks([10 * i for i in range(11)])	# label at 0, 10, ..., 100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.savefig("py3-cmp.png")
plt.show()


## cmp
#
# compare with py3.py, the x is from 0 to 100, but bar has width, so
# in py3.py, starting from -5 is good, since width is 8, half is 4,
# so -5 makes it has 1 unit abundance to the left, and 0 is in the
# middle of the bar
