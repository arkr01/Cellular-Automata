    # -*- coding: utf-8 -*-
"""
The Game of Life (GoL) module named in honour of John Conway

This module defines the classes required for the GoL simulation.

Created on Tue Jan 15 12:21:17 2019

@author: shakes
"""
import numpy as np
from scipy import ndimage


class GameOfLife:
    """
    Object for computing Conway's Game of Life (GoL) cellular machine/automata
    """

    def __init__(self, N=256, finite=False, fastMode=False):
        self.grid = np.zeros((N, N), np.uint)
        self.neighborhood = np.ones((3, 3), np.uint)  # 8 connected kernel
        self.neighborhood[1, 1] = 0  # do not count centre pixel
        self.finite = finite
        self.fastMode = fastMode
        self.aliveValue = 1
        self.deadValue = 0

    def getStates(self):
        """
        Returns the current states of the cells
        """
        return self.grid

    def getGrid(self):
        """
        Same as getStates()
        """
        return self.getStates()

    def evolve(self):
        """
        Given the current states of the cells, apply the GoL rules:
        - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        - Any live cell with two or three live neighbors lives on to the next generation.
        - Any live cell with more than three live neighbors dies, as if by overpopulation.
        - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
        """

        # n = len(self.getGrid())
        # weighted_sums = np.zeros((n, n), np.uint)
        # updated_grid = self.getGrid()

        # get weighted sum of neighbors
        # PART A & E CODE HERE
        weighted_sums = ndimage.convolve(self.getGrid(), self.neighborhood, mode='constant')

        # for i in range(n):  # rows
        #     for j in range(n):  # columns
        #         if i > 0:  # have top neighbours
        #             weighted_sums[i, j] += self.grid[i - 1, j]
        #             if j > 0:  # have left neighbours
        #                 weighted_sums[i, j] += self.grid[i, j - 1]
        #                 weighted_sums[i, j] += self.grid[i - 1, j - 1]
        #             if j < n - 1:  # have right neighbours
        #                 weighted_sums[i, j] += self.grid[i, j + 1]
        #                 weighted_sums[i, j] += self.grid[i - 1, j + 1]
        #         if i < n - 1:  # have bottom neighbours
        #             weighted_sums[i, j] += self.grid[i + 1, j]
        #             if j > 0:  # have left neighbours
        #                 weighted_sums[i, j] += self.grid[i + 1, j - 1]
        #                 if i == 0:  # stop over-counting when 0 < i < n - 1
        #                     weighted_sums[i, j] += self.grid[i, j - 1]
        #             if j < n - 1:  # have right neighbours
        #                 weighted_sums[i, j] += self.grid[i + 1, j + 1]
        #                 if i == 0:  # stop over-counting when 0 < i < n - 1
        #                     weighted_sums[i, j] += self.grid[i, j + 1]
        #
        # # implement the GoL rules by thresholding the weights
        # for i in range(n):
        #     for j in range(n):
        #         if self.getGrid()[i, j] == self.aliveValue:
        #             if weighted_sums[i, j] < 2 or weighted_sums[i, j] > 3:
        #                 updated_grid[i, j] = self.deadValue
        #         else:
        #             if weighted_sums[i, j] == 3:
        #                 updated_grid[i, j] = self.aliveValue

        # update the grid
        self.grid &= ~((weighted_sums < 2) | (weighted_sums > 3))  # if alive
        self.grid |= (weighted_sums == 3)  # if dead

    def insert_pattern(self, filename, index=(0, 0)):
        """ Insert GoL pattern defined in filename at starting index. """

        # Read and store file contents
        pattern_file = open(filename, "r")
        total_contents = pattern_file.readlines()
        pattern_file.close()

        # Get rid of name/author/descriptions
        actual_pattern = [line for line in total_contents if line[0] != '!']

        # Keep track of row number
        line_num = 0
        for line in actual_pattern:
            # Keep track of column number
            char_num = 0

            # Draw pattern
            for char in line:
                # File presents 'O' for alive and '.' for dead
                if char == 'O':
                    self.grid[index[0] + line_num, index[1] + char_num] = self.aliveValue
                char_num += 1
            line_num += 1


    def insertBlinker(self, index=(0, 0)):
        """
        Insert a blinker oscillator construct at the index position
        """
        self.grid[index[0], index[1] + 1] = self.aliveValue
        self.grid[index[0] + 1, index[1] + 1] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 1] = self.aliveValue

    def insertGlider(self, index=(0, 0)):
        """
        Insert a glider construct at the index position
        """
        self.grid[index[0], index[1] + 1] = self.aliveValue
        self.grid[index[0] + 1, index[1] + 2] = self.aliveValue
        self.grid[index[0] + 2, index[1]] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 1] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 2] = self.aliveValue

    def insertGliderGun(self, index=(0, 0)):
        """
        Insert a glider construct at the index position
        """
        self.grid[index[0] + 1, index[1] + 25] = self.aliveValue

        self.grid[index[0] + 2, index[1] + 23] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 25] = self.aliveValue

        self.grid[index[0] + 3, index[1] + 13] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 14] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 21] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 22] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 35] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 36] = self.aliveValue

        self.grid[index[0] + 4, index[1] + 12] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 16] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 21] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 22] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 35] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 36] = self.aliveValue

        self.grid[index[0] + 5, index[1] + 1] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 2] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 11] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 17] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 21] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 22] = self.aliveValue

        self.grid[index[0] + 6, index[1] + 1] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 2] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 11] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 15] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 17] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 18] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 23] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 25] = self.aliveValue

        self.grid[index[0] + 7, index[1] + 11] = self.aliveValue
        self.grid[index[0] + 7, index[1] + 17] = self.aliveValue
        self.grid[index[0] + 7, index[1] + 25] = self.aliveValue

        self.grid[index[0] + 8, index[1] + 12] = self.aliveValue
        self.grid[index[0] + 8, index[1] + 16] = self.aliveValue

        self.grid[index[0] + 9, index[1] + 13] = self.aliveValue
        self.grid[index[0] + 9, index[1] + 14] = self.aliveValue
