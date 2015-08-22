#!/usr/bin/env python
# Sets, with unique/distinct value
s = set()
s.add(1) # {1}
s.add(2) # {1, 2}
s.add(2) # still {1, 2}

x = len(s)	## still 2, 
y = 2 in s      # True
z = 3 in s	# False
