# -*- coding: utf-8 -*-
"""
Langton's Ant Implementation.

Created on Mon May 3 13:20:10 2021

@author: Adrian Rahul Kamal Rajkamal
"""

import numpy as np
import enum


class AntOrientation(enum.Enum):
    """ Enum for the possible orientations of the ant. """
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class LangtonAnt:
    """ Langton's Ant Representation and functionality. """

    def __init__(self, n, rule):
        self.grid = np.zeros((n, n), np.uint)
        self.x = n // 2  # current x position of the ant - start at middle
        self.y = n // 2  # current y position of the ant - start at middle
        self.orientation = AntOrientation.LEFT  # current orientation of the ant - start facing up
        self.rule = rule
        self.num_rules = len(self.rule)

    def get_states(self):
        """ Returns the current state of the grid. """
        return self.grid

    def move_left(self):
        """ Move left based on orientation of ant. """
        if self.orientation == AntOrientation.UP:
            self.x -= 1
            self.orientation = AntOrientation.LEFT
        elif self.orientation == AntOrientation.DOWN:
            self.x += 1
            self.orientation = AntOrientation.RIGHT
        elif self.orientation == AntOrientation.LEFT:
            self.y += 1
            self.orientation = AntOrientation.DOWN
        else:
            self.y -= 1
            self.orientation = AntOrientation.UP

    def move_right(self):
        """ Move right based on orientation of ant. """
        if self.orientation == AntOrientation.UP:
            self.x += 1
            self.orientation = AntOrientation.RIGHT
        elif self.orientation == AntOrientation.DOWN:
            self.x -= 1
            self.orientation = AntOrientation.LEFT
        elif self.orientation == AntOrientation.LEFT:
            self.y -= 1
            self.orientation = AntOrientation.UP
        else:
            self.y += 1
            self.orientation = AntOrientation.DOWN

    def evolve(self):
        """
        Given the current states of the cells, and the given rule string, apply the Langton's Ant
        rules.
        """
        # current value ('colour') of grid
        current = self.grid[self.x, self.y]

        # 'toggle' the colour of the square (i.e. shift to next colour)
        self.grid[self.x, self.y] = ((current + 1) % self.num_rules)

        # Move the ant based on rule string and colour of current square (before toggling)
        self.move_left() if self.rule[current] == "L" else self.move_right()
