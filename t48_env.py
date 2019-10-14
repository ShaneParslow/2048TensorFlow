import numpy as np
import gym
import time

import game


class Twenty48Gym(gym.Env):

    def __init__(self):
        self.game_instance = game.Twenty48()
        self.inv_move = 0
        self.scores = []  # List of 100 most recent scores
        self.avg_scores = []  # List of average score for all tests

    def step(self, action):
        previous_score = int(self.game_instance.score)
        previous_board = list(self.game_instance.board)

        #  Make move based on network output  #
        if action == 0:
            self.game_instance.shift_up()
        elif action == 1:
            self.game_instance.shift_right()
        elif action == 2:
            self.game_instance.shift_down()
        elif action == 3:
            self.game_instance.shift_left()
        else:
            raise ValueError("Invalid move {}".format(action))  # Network move out of bounds

        #  Reward calculation  #
        if previous_board != list(self.game_instance.board):  # Reward if a proper move was made
            reward = self.game_instance.score - previous_score
            self.inv_move = 0  # Reset network kill counter
        else:  # Record move with no effect
            self.inv_move += 1
            reward = 0

        return self.game_instance.board, reward, self.game_instance.hasLost or self.inv_move > 0, {}

    def reset(self):
        self.inv_move = 0
        self.scores.append(self.game_instance.score)
        self.scores = self.scores[-100:]
        self.game_instance = game.Twenty48()  # Reinstantiate to reset
        current_avg = np.average(self.scores)
        self.avg_scores.append(current_avg)
        print("\n{}".format(current_avg))
        return np.array(self.game_instance.board)

    def render(self, mode='human'):
        if(mode==human):
            import ui 
       	    ui.update_ui(self.game_instance)
            ui.window.update_idletasks()
            ui.window.update()
        #time.sleep(0.1)
