#!/usr/bin/env python3

import tensorflow as tf
import numpy as np

class twenty48():
    def __init__(self, size):
        #create empty board filled with zeroes of size provided
        self.board = [[0] * size] * size

game = twenty48(3)
print(np.matrix(game.board))
