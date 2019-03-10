#!/usr/bin/env python3
import numpy as np  #Seemingly only required for windows
import tkinter as tk

import game
import ui


t48 = game.Twenty48()
ui.init_ui(t48)

while True:
    print(np.matrix(t48.board))
    ui.update_ui(t48)
    tk.mainloop()
