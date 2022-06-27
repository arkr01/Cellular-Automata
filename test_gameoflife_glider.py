# -*- coding: utf-8 -*-
"""
Game of life script with animated evolution

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""

import conway
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.switch_backend('QT5Agg')

N = 1050

# create the game of life object
life = conway.GameOfLife(N)
# life.insertGliderGun()
life.insert_pattern(filename="deepcell.cells")
cells = life.getStates()  # initial state

# -------------------------------
# plot cells

fig = plt.figure()

plt.gray()

img = plt.imshow(cells, animated=True)


def animate(i):
    """perform animation step"""
    global life
    life.evolve()
    cellsUpdated = life.getStates()

    img.set_array(cellsUpdated)

    return img,


interval = 1  # ms

# animate 24 frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=24, interval=interval, blit=True)

plt.show()
