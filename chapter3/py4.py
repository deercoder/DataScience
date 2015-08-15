#!/usr/bin/env python

from matplotlib import pyplot as plt

mentions = [500, 505]
years = [2013, 2014] # the label is 2013 and 2014

plt.bar([2012.6, 2013.6], mentions, 0.8) # but the values should get the actual value in the middle
plt.xticks(years) # the real labeL
plt.ylabel("# of times I heard someone say 'data science'")

## all the above is OK for drawing, but it will label x with [0, 1], and give an offset of +2.013e3
# add this to fix
plt.ticklabel_format(useOffset=False) # this use to make it not start from 0


### the following can be commented for another plotting
plt.axis([2012.5, 2014.5, 499, 506]) # this makes y not start from 0, x is quite the same as before except the above offset setting
plt.title("Look at the 'Huge' Increase!")

# shows the item
plt.show()

# if y is not starting from 0, then it is easy for misleading. In this case, there is no big difference, but if not starting from 0,
# then we might see a big difference there
