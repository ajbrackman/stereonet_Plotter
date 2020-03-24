#This version is for single strike/dip data entry

#Import packages
import matplotlib.pyplot as plt
import numpy as np
import mplstereonet
from six.moves import input as raw_input
import csv
from tkinter import *
"""
gui = input("Do you want to launch the (non-functional) test GUI? (Y|y|yes)")
if gui in ['Y', 'y','yes']:
window = Tk()

    menu = Menu(window)
    menu_items = Menu(menu)
    menu_items.add_command(label='Plot Planes')
    menu_items.add_separator()
    menu_items.add_command(label='Plot Poles')
    menu_items.add_separator()

    menu.add_cascade(label='File', menu=menu_items)

    window.title("welcome to the Stereonet Plotter!")
    window.geometry('640x480')

    input_line1 = Label(window, text="Please enter a strike in azimuth i.e. 212 or quadrant (i.e. N30W) format: ")
    input_line1.grid(column=0,row=0)

    strk = Entry(window,width=10)
    strk.grid(column=1,row=0)
    strike = strk.get()

    def clicked():
        strike_confirm = "You confirmed a strike of: " + strk.get()
        input_line1.configure(text= strike_confirm)
        strike_button = Button(window, text="Confirm Entry", command=clicked)
        strike_button.grid(column=2,row=0)

        input_line2 = Label(window, text="Please enter a dip value in degrees: ")
        input_line2.grid(column=0,row=1)

        dip_field = Entry(window,width=10)
        dip_field.grid(column=1,row=1)
        dip = dip_field.get()
        def clicked1():
            dip_confirm = "You confirmed a dip of " + dip_field.get()
            input_line2.configure(text= dip_confirm)
            dip_button = Button(window, text="Confirm Entry", command=clicked1)
            dip_button.grid(column=2,row=1)

            window.config(menu=menu)
            window.mainloop()
else:
"""
# Create equal area stereonet
fig = plt.figure()
ax = fig.add_subplot(111, projection='stereonet')

strike = input("Enter a strike in azimuth (i.e. 212) or quadrant (i.e. N30W) format: ")
dip = int(input("Enter a dip value in degrees and press ENTER: "))

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
