# This version is used for entering a single strike and dip.

import matplotlib.pyplot as plt
import numpy as np
import mplstereonet
import csv

# Create equal area stereonet
fig = plt.figure()
ax = fig.add_subplot(111, projection='stereonet')

# Create column reader and open CSV file. Then initialize empty lists for strikes & dips
col_reader = csv.reader(open('strikesdips.csv', 'rb'), delimiter=",")
strikes, dips = [],[]

# Append CSV values into variables
for row in col_reader:
    strikes.append(int(row[0]))
    dips.append(int(row[1]))

# Self-explanatory
print "Strikes: ", strikes
print "Dips: ", dips

# Initialize length variables for next steps.
# These can be compared for testing purposes
strikesLength = len(strikes)
dipsLength = len(dips)

if strikesLength != dipsLength:
    print "Your data has a non-matching amount of strikes and dips. Please check your \
    data file and try again."
    exit()

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
