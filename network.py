# FUCK THIS FUCKING FUCK PIECE OF SHIT FUCK #

import keras as ks
from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory
from tkinter import TclError
import matplotlib.pyplot as plt
import t48_env

global gym_env
gym_env = t48_env.Twenty48Gym()


def init_network():
    # Keras initial model and layers
    model = ks.Sequential()
    model.add(ks.layers.Flatten(input_shape=(1,4,4)))
    model.add(ks.layers.Dense(100))
    model.add(ks.layers.Activation('relu'))
    model.add(ks.layers.Dense(100))
    model.add(ks.layers.Activation('relu'))
    model.add(ks.layers.Dense(100))
    model.add(ks.layers.Activation('relu'))
    model.add(ks.layers.Dense(100))
    model.add(ks.layers.Activation('relu'))
    model.add(ks.layers.Dense(100))
    model.add(ks.layers.Activation('relu'))
    model.add(ks.layers.Dense(100))
    model.add(ks.layers.Activation('relu'))
    model.add(ks.layers.Dense(100))
    model.add(ks.layers.Activation('relu'))
    model.add(ks.layers.Dense(100))
    model.add(ks.layers.Activation('relu'))
    model.add(ks.layers.Dense(100))
    model.add(ks.layers.Activation('relu'))
    model.add(ks.layers.Dense(100))
    model.add(ks.layers.Activation('relu'))
    model.add(ks.layers.Dense(100))
    model.add(ks.layers.Activation('relu'))
    model.add(ks.layers.Dense(100))
    model.add(ks.layers.Activation('relu'))
    model.add(ks.layers.Dense(100))
    model.add(ks.layers.Activation('relu'))
    model.add(ks.layers.Dense(100))
    model.add(ks.layers.Activation('relu'))
    model.add(ks.layers.Dense(100))
    model.add(ks.layers.Activation('relu'))
    model.add(ks.layers.Dense(4))
    model.add(ks.layers.Activation('linear'))
    print(model.summary())

    memory = SequentialMemory(limit=50000, window_length=1)
    policy = EpsGreedyQPolicy()  # THIS MIGHT BE WRONG
    agent = DQNAgent(model=model, nb_actions=4, memory=memory, nb_steps_warmup=100,
                     target_model_update=1e-2, policy=policy)
    agent.compile(ks.optimizers.Adam(lr=1e-3))
    return agent


def train_network(agent):
    agent.fit(gym_env, nb_steps=float(20000*30), visualize=True, nb_max_episode_steps=0)
    return gym_env


dqn_agent = init_network()
try:
    train_network(dqn_agent)
except (KeyboardInterrupt, TclError):
    dqn_agent.save_weights('dqn_t48_weights.h5f', overwrite=True)
    # print(len(range(1, len(gym_env.avg_scores))))
    # print(gym_env.avg_scores)
    plt.scatter(range(1, len(gym_env.avg_scores) + 1), gym_env.avg_scores)
    plt.show()
    exit()
dqn_agent.save_weights('dqn_t48_weights.h5f', overwrite=True)
plt.scatter(range(1, len(gym_env.avg_scores) + 1), gym_env.avg_scores)
plt.show()
dqn_agent.test(gym_env, nb_episodes=5, visualize=True)
