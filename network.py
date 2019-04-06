import keras as ks
import numpy as np


def init_network(game_instance):
    model = ks.Sequential()
    model.add(ks.layers.Dense(64, input_dim=game_instance.size, activation="relu"))  # Hidden layer 1
    model.add(ks.layers.Dense(64, activation="relu"))  # Hidden layer 2
    model.add(ks.layers.Dense(1, activation="linear"))  # 1 list of 4 possible movements for output

    model.compile(loss="mse", optimizer=ks.optimizers.Adam())
    return model


def predict_network(game_instance, model):
    model.summary()
    print(model.predict(np.array(game_instance.board)))
    return model.predict(game_instance.board)
