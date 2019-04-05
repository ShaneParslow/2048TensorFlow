import tensorflow as tf
import numpy as np  #Seemingly only required for windows
import tkinter as tk

import game

t48 = game.Twenty48(dimensions=5)

session = tf.Session()


trainer = tf.train.GradientDescentOptimizer(0.01)

net_in = tf.placeholder(tf.float64, shape=(t48.size, t48.size))
hidden_layer = tf.layers.Dense(units=2)

output_in = hidden_layer(net_in)
output_layer = tf.layers.Dense(units=1)
output = output_layer(output_in)

init = tf.global_variables_initializer()
session.run(init)  # Run the variable initializer

while not t48.hasLost: # Loop network for entire
    suggested_moves = session.run(output, feed_dict={net_in: t48.board})
    print(np.matrix(t48.board))
    print(suggested_moves)
    max_value = max(suggested_moves)
    move_direction = list(suggested_moves).index(max_value)

    previous_board = t48.board

    if move_direction == 0:
        t48.shift_up()
    elif move_direction == 1:
        t48.shift_right()
    elif move_direction == 2:
        t48.shift_down()
    elif move_direction == 4:
        t48.shift_left()

    if t48.board == previous_board: # If the network keeps going in the same direction just kill it
        break

'''
while not lost
    sess run (t48.board) # Run network with current board

loss = 1/t48.score
sess run (training) # Minimize loss based on score 
'''
