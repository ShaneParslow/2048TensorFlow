import numpy as np

import game


class Twenty48Gym:
    def __init__(self):
        self.game_instance = game.Twenty48()

    def step(self, action):
        previous_score = self.game_instance.score
        if action == 0:
            self.game_instance.shift_up()
        elif action == 1:
            self.game_instance.shift_right()
        elif action == 2:
            self.game_instance.shift_down()
        elif action == 3:
            self.game_instance.shift_left()
        else:
            print("who would've thought, this didn't work!")
        reward = self.game_instance.score - previous_score

        return np.array(self.game_instance.board), reward, self.game_instance.hasLost, None

    def reset(self):
        self.game_instance = game.Twenty48  # Reinstantiate to reset
        return np.array(self.game_instance.board)
