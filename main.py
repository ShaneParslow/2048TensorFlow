#!/usr/bin/env python3
import numpy as np  #Seemingly only required for windows

import game
import ui


t48 = game.Twenty48()
while True:
    print(np.matrix(t48.board))
    print(t48.score)
    move = input("Direction to move: ")
    if move == "u":
        t48.shift_up()
    elif move == "d":
        t48.shift_down()
    elif move == "l":
        t48.shift_left()
    elif move == "r":
        t48.shift_right()
    else:
        print("Invalid move")
