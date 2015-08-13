#!/usr/bin/env python
# control flow,

if 1 > 2:
	message = "if only 1 were greater than two ..."
elif 1 > 3:
	message = "elif stands for 'else if'"
else:
	message = "when all else fails use else(if you want to)"

print message

# write an ternary if-then-else on one line
x = 22
parity = "even" if x % 2 == 0 else "odd"	## if then "even", else is "odd"

# while
x = 0
while x < 10:
	print x, "is less than 10"
	x += 1

# use for/in more often
for x in range(10):
	print x, "is less than 10"


# use continue or break for complex control
for x in range(10):
	if x == 3:
		continue # go to next iteration without any executing of this loop
	if x == 5:
		break # quit entirely of this loop
	print x
