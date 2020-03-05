# This version is used for reading strike and dip data from a file (strikesdips.csv)

import matplotlib.pyplot as plt
import numpy as np
import mplstereonet
import csv
from tabulate import tabulate

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
        strikes.append(row[0])
        dips.append((int(row[1])))

# Initializing a couple things
azimuths = []
strikesLength = len(strikes)

# Fill the azimuth array by with parse_azimuth function to check for quadrant entries
i=0
while i < strikesLength:
    azimuths.append(mplstereonet.parse_azimuth(strikes[i]))
    i += 1

# Create 2D array of strikes and dips
strikedip = zip(azimuths,dips)

# Self-explanatory
print "Total number of measurements: %d"%(len(strikes))
print tabulate(strikedip, headers, tablefmt="grid")

# Initialize length variables for next steps.
# These can be compared for testing purposes
# dipsLength = len(dips)

# Create N variable for loop
N = len(strikes)

# Generate color map for entries
# See https://matplotlib.org/gallery/color/colormap_reference.html &
# https://matplotlib.org/tutorials/colors/colormaps.html
cmap = plt.cm.get_cmap("rainbow", N+1)

# Increment from 0 to N through strikes & dips, plotting poles, planes, & rakes
i=0
for i in range(N):
    ax.plane(azimuths[i], dips[i], 'g-', linewidth=2, color=cmap(i))
    ax.pole(azimuths[i], dips[i], 'g^', markersize=12, color=cmap(i))
    ax.rake(azimuths, dips, -25)

#draw grid on stereonet
ax.grid()

#display plot
plt.show()
