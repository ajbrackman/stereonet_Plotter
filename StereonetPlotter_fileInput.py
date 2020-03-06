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
# dipsLength = len(dips) # This is unnecessary at the moment, unused

# Parse all strike inputs and convert to azimuth if necessary.
for i in range(strikesLength):
    azimuths.append(mplstereonet.parse_azimuth(strikes[i]))

# Generate color map for entries
# See https://matplotlib.org/gallery/color/colormap_reference.html &
# https://matplotlib.org/tutorials/colors/colormaps.html
cmap = plt.cm.get_cmap("hsv", strikesLength+1)

# Plot poles or planes per user input
poles = raw_input("Do you want to plot poles instead of planes? (Y/N): ")
if poles in ['Y','y','yes']:
    i=0
    for i in range(strikesLength):
        ax.pole(azimuths[i], dips[i], 'g^', marker='o', markersize=8, color=cmap(i))
if poles in ['N','n','no']:
    i=0
    for i in range(strikesLength):
        ax.plane(azimuths[i], dips[i], 'g-', linewidth=2, color=cmap(i))

# Give option to plot rakes. Say No if only plotting poles
rakes = raw_input("Do you want to plot the rakes? (Y/N)")
if rakes in ['Y','y','yes']:
    ax.rake(azimuths, dips, -25)
if rakes in ['N','n','']:
    print "I won't plot the rakes"

# Gives option to contour poles
do_contour = raw_input("Do you want to contour the poles? (Y/N)")
if do_contour in ['Y','y','yes']:
    cax = ax.density_contourf(azimuths,dips, measurement='poles', cbar='rainbow') #cbar arg doesn't seem to do anything
    fig.colorbar(cax)
if do_contour in ['N','n','no']:
    print "I won't plot a contour map"
    
# Create 2D array of strikes and dips
strikedip = zip(azimuths,dips)

# Self-explanatory
print "Total number of measurements: %d"%(len(strikes))
print tabulate(strikedip, headers, tablefmt="grid")

# Draw grid on stereonet and show plot
ax.grid()
plt.ion()
plt.show()
plt.pause(0.01)
raw_input("Press ENTER to continue")

#plt.show() #this one doesn't work, not sure how to re-open matplotlib window...

#draw grid on stereonet
#ax.grid()
#display plot
#plt.show()
#print "Do you want to plot anything else?"
