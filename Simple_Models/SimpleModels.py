# This is just a simple model that does nothing.

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.activations import relu, softmax

import numpy as np

# Data
Train=np.array([[0,0,0],[1,0,1],[1,0,0], [0,1,0]])
Practical=np.array([[1,1,1]])

print("Shapes:\nTrain Shape: {t}\nPractical Shape: {p}".format(t=Train.shape, p=Practical.shape))

# Model
model=Sequential()
model.add(Flatten(input_shape=(3,)))
model.add(Dense(6, activation=relu))
model.add(Dense(6, activation=softmax))
model.compile(optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"])

