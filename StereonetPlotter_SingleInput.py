import matplotlib.pyplot as plt
import numpy as np
import mplstereonet
import csv

fig = plt.figure()
ax = fig.add_subplot(111, projection='stereonet')



strike = input("Enter a strike (in AZ or quadrant [i.e. N30E]) and press ENTER: ")
dip = input("Enter a dip and direction [i.e. 55SE] and press ENTER: ")

ax.plane(strike, dip, 'g-', linewidth=2)
ax.pole(strike, dip, 'g^', markersize=15, marker="x")
ax.rake(strike, dip, -25)
ax.grid()

plt.show()
