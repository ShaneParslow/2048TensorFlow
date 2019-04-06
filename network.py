import keras as ks
from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

import t48_env


def init_network():
    # Keras initial model and layers
    model = ks.Sequential()
    model.add(ks.layers.Dense(64, input_shape=(1, 4, 4), activation="relu"))  # Hidden layer 1
    #model.add(ks.layers.Dense(64, activation="relu"))  # Hidden layer 2
    #model.add(ks.layers.Dense(64, activation="relu"))  # Hidden layer 3
    model.add(ks.layers.Dense(1, activation="linear"))  # 1 list of 4 possible movements for output
    model.add(ks.layers.Flatten())

    print(model.summary())

    memory = SequentialMemory(limit=50000, window_length=1)
    policy = BoltzmannQPolicy()
    agent = DQNAgent(model=model, nb_actions=4, memory=memory, nb_steps_warmup=500,
                     target_model_update=1e-2, policy=policy)
    agent.compile(ks.optimizers.Adam(lr=1e-3), metrics=['mae'])
    return agent


def train_network(agent):
    env = t48_env.Twenty48Gym()
    agent.fit(env, nb_steps=100000)


workpls = init_network()
train_network(workpls)
