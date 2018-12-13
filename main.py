#!/usr/bin/env python3

import tensorflow as tf
import numpy as np

class twenty48():
	def __init__(self, dimensions):
		self.size = dimensions

		#create empty board filled with zeroes of size provided
		self.board = [[0] * self.size] * self.size

	def addToBoard(num):#add numbers to board. 90% chance of 2, 10% chance of 4.
		chosen = []#list of coordinates already chosen, so that they aren't picked again

		for i in range(num):
			coord = np.random.randint(self.size + 1, size=2)#add 1 because numpy is non-inclusive
			chosen.append(coord)

			value = 4 if np.random.rand() > 0.9 else 2#90% chance of tile with 2, 10% chance of 4

game = twenty48(4)
print(np.matrix(game.board))
