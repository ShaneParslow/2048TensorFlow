#!/usr/bin/env python3

import tensorflow as tf
import numpy as np

class twenty48():
	def __init__(self, dimensions):
		self.size = dimensions

		#create empty board filled with zeroes of size provided
		self.board = [[0 for i in range(self.size)] for j in range(self.size)]
		self.addToBoard(2)

	#GAZE UPON THIS METHOD WITH FEAR, FOR IT IS MUCH MORE INTIMIDATING THAN IT LOOKS
	#also I sacrificed my sanity to it
	def addToBoard(self, num):#add numbers to board. 90% chance of 2, 10% chance of 4.
		for i in range(num):
			collision = True

			while collision:#keep repeating until coordinate is selected that isnt already chosen and is empty
				x_coord = np.random.randint(self.size)
				y_coord = np.random.randint(self.size)
				value = 4 if np.random.rand() > 0.9 else 2#90% chance of tile with 2, 10% chance of 4

				if self.board[y_coord][x_coord] == 0:
					collision = False#good to select next coordinate
					self.board[x_coord][y_coord] = value#add coord and value to board

game = twenty48(4)
print(np.matrix(game.board))
