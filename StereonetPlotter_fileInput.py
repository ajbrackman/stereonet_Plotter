# This version is used for reading strike and dip data from a file (strikesdips.csv)

import matplotlib.pyplot as plt
import numpy as np
import mplstereonet
import csv
import pandas

# Create equal area stereonet
fig = plt.figure()
ax = fig.add_subplot(111, projection='stereonet')

# Initialize lists for data
strikes, dips = [],[]

# Read strike and dip data from file, skipping headers
with open('strikesdips.csv','r') as csvfile:
    csvreader = csv.reader(csvfile)
    headers = csvreader.next() # grabs header row
    for row in csvreader:
        strikes.append(int(row[0]))
        dips.append((int(row[1])))

# Self-explanatory
# Next step here is to recombine and display them neatly in console window
print "Total number of measurements: %d"%(len(strikes))
print headers[0], strikes
print headers[1], dips

# Initialize length variables for next steps.
# These can be compared for testing purposes
strikesLength = len(strikes)
dipsLength = len(dips)

# print strikesLength, dipsLength

# PLACEHOLDER FOR LIST LENGTH COMPARISON

#Create N variable for loop
N = len(strikes)

# Generate color map for entries
# See https://matplotlib.org/gallery/color/colormap_reference.html &
# https://matplotlib.org/tutorials/colors/colormaps.html
cmap = plt.cm.get_cmap("gist_rainbow", N+1)

# Increment from 0 to N through strikes & dips, plotting poles, planes, & rakes
i=0
for i in range(N):
    ax.plane(strikes[i], dips[i], 'g-', linewidth=2, color=cmap(i))
    ax.pole(strikes[i], dips[i], 'g^', markersize=12, color=cmap(i))
    ax.rake(strikes, dips, -25)

#draw grid on stereonet
ax.grid()

#display plot
plt.show()
