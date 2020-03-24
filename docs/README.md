# First attempt at creating a stereonet plotting program in python using mplstereonet

Both versions work with python3 on linux. The easiest way to run these on windows is to use Anaconda2 or Anaconda3

Required Packages: mplstereonet, matplotlib, numpy, csv, tabulate

Two versions currently exist:
## StereonetPlotter_fileinput.py
This script takes a CSV (strikesdips.csv) with strikes (in quadrant or azimuth) format and dip values (in degrees), prints these to the console and plots planes and poles on an equal area stereonet.

This version now has some very basic logic. Can choose which data to plot and can contour poles (don't try to contour planes!)

## StereonetPlotter_SingleInput.py
This script prompts the user to enter a strike (in quadrant or azimuth) and a dip value (in degrees) and then plots the plane and pole on an equal area stereonet using a new color for each entry.
