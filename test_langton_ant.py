# -*- coding: utf-8 -*-
"""
Langton's Ant Simulation.

Created on Mon May 3 13:20:20 2021

@author: Adrian Rahul Kamal Rajkamal
"""

from langton_ant import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

plt.switch_backend('QT5Agg')  # For higher-quality animations

n = 100

# Change here for different patterns!
# From Langton's Ant Wikipedia - Creates a filled triangle shape that grows and moves."
rule = "RRLLLRLLLRRR"

# Change here for different colours! Ensure the number of colours is >= len(rule)
my_colours = ListedColormap(['xkcd:purple', 'xkcd:green', 'xkcd:blue', 'xkcd:pink', 'xkcd:brown',
                             'xkcd:red', 'xkcd:light blue', 'xkcd:teal', 'xkcd:orange',
                             'xkcd:light green', 'xkcd:magenta', 'xkcd:yellow'], N=len(rule))

# Make the ant!
ant = LangtonAnt(n, rule)
cells = ant.get_states()  # initial state

# plot cells
fig = plt.figure()
img = plt.imshow(cells, animated=True, vmin=0, vmax=my_colours.N, cmap=my_colours)


def animate(i):
    """ Perform animation step. """
    global ant
    # Speed up animation by calling evolve (i.e. updating to the next state of the grid) several
    # times per animation step
    for i in range(100):
        ant.evolve()
    updated_cells = ant.get_states()
    img.set_array(updated_cells)
    return img,


interval = 1  # ms

# animate 24 frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=24, interval=interval, blit=True)
plt.show()
