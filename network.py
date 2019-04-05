import tensorflow as tf
import numpy as np  #Seemingly only required for windows
import tkinter as tk

import game

# Main classes
t48 = game.Twenty48(dimensions=4)
session = tf.Session()

# Training
score = tf.placeholder(dtype=tf.float32)
loss = tf.math.divide(1, score) # Loss gets lower as score increases
loss_sub = tf.get_variable('loss_sub', dtype=tf.float32, initializer=tf.random_normal((1, 224, 224, 3)))
final_loss = tf.math.subtract(loss_sub, loss)

optimizer = tf.train.GradientDescentOptimizer(0.01)
trainer = optimizer.minimize(final_loss)

# Layers
net_in = tf.placeholder(tf.float64, shape=(t48.size, t48.size))
hidden_layer = tf.layers.Dense(units=2)
output_in = hidden_layer(net_in)
output_layer = tf.layers.Dense(units=1)
output = output_layer(output_in)

# Initialize tf
init = tf.global_variables_initializer()
session.run(init)  # Run the variable initializer

# Training loop
for i in range(100000):
    while not t48.hasLost: # Loop network until lost
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
    loss_value = session.run((trainer, loss), feed_dict={score: t48.score+1})
    print(loss_value)
    t48.__init__()  # Reset board

'''
while not lost
    sess run (t48.board) # Run network with current board

loss = 1/t48.score
sess run (training) # Minimize loss based on score 
'''
