#This version is for single strike/dip data entry

#Import packages
import matplotlib.pyplot as plt
import numpy as np
import mplstereonet
from six.moves import input as raw_input
import csv

# Create equal area stereonet
fig = plt.figure()
ax = fig.add_subplot(111, projection='stereonet')

strike = raw_input("Enter a strike in azimuth (i.e. 212) or quadrant (i.e. N30W) format: ")
dip = input("Enter a dip value in degrees and press ENTER: ")

# Parse strike entry and convert to azimuth as necessary.
# Print for testing & verification
azimuth = int(mplstereonet.parse_azimuth(strike))
print("Azimuth bearing: ", azimuth)

# Calculate dip direction per RHR.
# This is supposedly included with mplstereonet as strike2_dipdirection, but isn't working
dip_direction = azimuth + 90
if dip_direction > 360:
    dip_direction -= 360
print("Dip ", dip, " degrees, Dip Direction: ", dip_direction, " degrees") # Print dip angle and direction (in azimuth)

# Plot everyt)hing
ax.plane(azimuth, dip, 'g-', linewidth=2)
ax.pole(azimuth, dip, 'g^', markersize=15, marker="x")
ax.rake(azimuth, dip, -25)

ax.grid() # This draws the grid on the stereonet

plt.show() # What do you think this does?
