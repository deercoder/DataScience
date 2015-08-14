#!/usr/bin/env python
from matplotlib import pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01) # t is some values
s = np.sin(2*np.pi*t) # 2*pi*t
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True) # draw some grid/lines
plt.savefig("test.png")
plt.show()
