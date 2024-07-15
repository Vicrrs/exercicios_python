#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import mlflow
import mlflow.keras

class ModelTrainer:
    def train(self, X_train, y_train, epochs=None, learning_rate=None):
        raise NotImplementedError

    def predict(self, X_test):
        raise NotImplementedError

class NeuralNetworkTrainer(ModelTrainer):
    def __init__(self, input_dim, layers=[64, 64], learning_rate=0.001):
        self.model = Sequential()
        for units in layers:
            self.model.add(Dense(units, activation='relu', input_dim=input_dim if not self.model.layers else None))
        self.model.add(Dense(1, activation='sigmoid'))
        self.model.compile(optimizer=Adam(learning_rate=learning_rate), loss='binary_crossentropy', metrics=['accuracy'])

    def train(self, X_train, y_train, epochs=10):
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=32, validation_split=0.2, verbose=1)

    def predict(self, X_test):
        return (self.model.predict(X_test) > 0.5).astype("int32")

