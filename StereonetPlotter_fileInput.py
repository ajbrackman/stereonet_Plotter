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

# Generate color map for entries
# See https://matplotlib.org/gallery/color/colormap_reference.html &
# https://matplotlib.org/tutorials/colors/colormaps.html
cmap = plt.cm.get_cmap("rainbow", strikesLength+1)

# Parse entries to azimuth and write to list.
# Plot each plane and pole on the stereonet
for i in range(strikesLength):
    azimuths.append(mplstereonet.parse_azimuth(strikes[i]))
    ax.plane(azimuths[i], dips[i], 'g-', linewidth=2, color=cmap(i))
    ax.pole(azimuths[i], dips[i], 'g^', markersize=12, color=cmap(i))

ax.rake(azimuths, dips, -25) # Plot the rakes (needs to be done outside loop)

# Create 2D array of strikes and dips
strikedip = zip(azimuths,dips)

# Self-explanatory
print "Total number of measurements: %d"%(len(strikes))
print tabulate(strikedip, headers, tablefmt="grid")

#draw grid on stereonet
ax.grid()

#display plot
plt.show()
