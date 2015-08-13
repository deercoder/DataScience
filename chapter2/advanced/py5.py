#!/usr/bin/env python
# Regular expression

import re
print all([	# result is True because all is True
	not re.match("a", "cat"), # True, cat not start with a
	re.search("a", "cat"), # True, cat has an "a" in it
	not re.search("c", "dog"), # dog don't have "c" in it
	3 == len(re.split("[ab]", "carbs")), # split to c, r, s, so 3
	"R-D-" == re.sub("[0-9]", "-", "R2D2") #replace digit with -
	])
