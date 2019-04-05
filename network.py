import tensorflow as tf
import numpy as np  #Seemingly only required for windows
import tkinter as tk

import game

# Main classes
t48 = game.Twenty48(dimensions=4)
session = tf.Session()

# Training
loss = tf.placeholder(dtype=tf.float32) # Tensor to give trainer
loss_sub = tf.get_variable('loss_sub', dtype=tf.float32, initializer=tf.random_normal((1, 224, 224, 3)))
final_loss = tf.math.subtract(loss_sub, loss)

optimizer = tf.train.AdamOptimizer()
trainer = optimizer.minimize(final_loss)

# Layers
net_in = tf.placeholder(tf.float64, shape=(t48.size, t48.size))
dense1 = tf.layers.dense(inputs=net_in, units=2)
dense2 = tf.layers.dense(inputs=dense1, units=2)
output = tf.layers.dense(inputs=dense2, units=1)

# Initialize tf
init = tf.global_variables_initializer()
session.run(init)  # Run the variable initializer

# Training loop
for i in range(10000):
    i=0
    while not t48.hasLost:  # Loop network until lost
        suggested_moves = session.run(output, feed_dict={net_in: t48.board})
        #print(np.matrix(t48.board))
        #print(suggested_moves)
        previous_score = int(t48.score)
        move_direction = np.argmax(suggested_moves)  # Select best move

        previous_board = t48.board

        if move_direction == 0:
            t48.shift_up()
        elif move_direction == 1:
            t48.shift_right()
        elif move_direction == 2:
            t48.shift_down()
        elif move_direction == 4:
            t48.shift_left()
        final_score = int(t48.score)

        if t48.board == previous_board: # If the network keeps going in the same direction just kill it
            i += 1
            session.run((trainer, loss), feed_dict={loss: 999999}) # This is dumb
        if i > 20: # Kill the run if it keeps doing the same thing
            break
        session.run((trainer, loss,), feed_dict={loss:final_score-previous_score})
    print(final_score-previous_score)
    t48.__init__()  # Reset board

'''
while not lost
    sess run (t48.board) # Run network with current board

loss = 1/t48.score
sess run (training) # Minimize loss based on score 
'''
