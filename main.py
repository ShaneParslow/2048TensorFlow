#!/usr/bin/env python3
import numpy as np  #Seemingly only required for windows
import tkinter as tk

import game
import ui


t48 = game.Twenty48()
ui.init_ui(t48)

while True:
    print(np.matrix(t48.board))
    while True:
        ui.update_ui(t48)
        ui.window.update_idletasks()
        ui.window.update()
