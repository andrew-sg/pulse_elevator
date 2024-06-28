"""
This document tests animation functionality and seeks to replicate 
fig 2 in the pulse elevator paper:
https://eprints.gla.ac.uk/276593/1/276593.pdf 
@author ASG
Created 28/06/24
Changelog:

TODO: Add acceleration equations
"""


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

t_end = 1
steps = 200
interval = (t_end/steps)
dt = t_end/steps

fig, ax = plt.subplots()
t = np.linspace(0, t_end, steps)

# The bucket
f = 1 # frequency of sinusoidal motion
a = 10 # amplitude of sinusoidal motion in mm
z2 = a * np.sin(2*np.pi*f * t) # vertical displacement of bucket

# The particle
g = -9.81 # force of gravity
gamma = round(((a/1000) * ((2*np.pi*f)**2))/g,2) # relative acceleration
v = 12 # initial vertical velocity  
z = g * t**2 / 2 + v * t # vertical displacement of particle

scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'gamma = {gamma} m/s^2')
line2 = ax.plot(t[0], z2[0], label=f'f = {f} Hz')[0]
ax.set(xlim=[0, t_end], ylim=[-10, 10], xlabel='Time [s]', ylabel='Z [mm]')
ax.legend()


def update(frame):
    # for each frame, update the data stored on each artist.
    x = t[:frame]
    y = z[:frame]
    # update the scatter plot:
    data = np.stack([x, y]).T
    scat.set_offsets(data)
    # update the line plot:
    line2.set_xdata(t[:frame])
    line2.set_ydata(z2[:frame])
    return (scat, line2)


ani = animation.FuncAnimation(fig=fig, func=update, frames=steps, interval=interval)
plt.show()