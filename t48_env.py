import numpy as np
import gym

import game


class Twenty48Gym(gym.Env):

    def __init__(self):
        self.game_instance = game.Twenty48()

    def step(self, action):
        previous_score = int(self.game_instance.score)
        previous_board = list(self.game_instance.board)
        if action == 0:
            self.game_instance.shift_up()
        elif action == 1:
            self.game_instance.shift_right()
        elif action == 2:
            self.game_instance.shift_down()
        elif action == 3:
            self.game_instance.shift_left()
        else:
            raise ValueError("Invalid move {}".format(action))
        if previous_board != list(self.game_instance.board):  # Reward if a proper move was made
            reward = self.game_instance.score - previous_score
        elif self.game_instance.hasLost:
            reward = -10
        else:  # Move did nothing
            reward = -1

        return np.array(self.game_instance.board), reward, self.game_instance.hasLost, {}

    def reset(self):
        self.game_instance = game.Twenty48()  # Reinstantiate to reset
        return np.array(self.game_instance.board)
