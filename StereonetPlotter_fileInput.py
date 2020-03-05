# This version is used for entering a single strike and dip.

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
    headers = csvreader.next() # skips header row
    for row in csvreader:
        strikes.append(int(row[0]))
        dips.append((int(row[1])))

# Self-explanatory
print headers
print "Strikes :", strikes
print "Dips: ", dips
print "Total number of measurements: %d"%(len(strikes)) # Print length of strike list
# Initialize length variables for next steps.
# These can be compared for testing purposes
strikesLength = len(strikes)
dipsLength = len(dips)

# print strikesLength, dipsLength

# This doesn't work yet because if CSV does not have equal number of strikes & dips, program breaks at csvreader
#if strikesLength != dipsLength:
#    print "Your data has a non-matching amount of strikes and dips. Please check your \
#    data file and try again."
#    exit()
#else:

#Create N variable for loop
N = len(strikes)

#generate color map for entries
cmap = plt.cm.get_cmap("hsv", N+1)

# Increment from 0 to N through strikes & dips, plotting poles and planes
i=0
for i in range(N):
    ax.plane(strikes[i], dips[i], 'g-', linewidth=2, color=cmap(i))
    ax.pole(strikes[i], dips[i], 'g^', markersize=12, color=cmap(i))
    ax.rake(strikes, dips, -25)

#draw grid on stereonet
ax.grid()

#display plot
plt.show()
