#!/usr/bin/env python3
import numpy as np  #Seemingly only required for windows

import game


t48 = game.Twenty48()
print(np.matrix(t48.board))
print(t48.score)
