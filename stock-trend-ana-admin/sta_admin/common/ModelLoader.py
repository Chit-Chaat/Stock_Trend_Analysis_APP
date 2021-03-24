__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '3/24/2021 2:22 AM'

import os
from datetime import datetime, timedelta

import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

from StockDataGenerator import StockDataGenerator

MODEL_SAVED_PLACE = "\model"
MODEL_NAME = "model_weights.h5"


class StockModel:
    def __init__(self, stock):
        self._stock = stock
        self._ticker = self._stock.get_ticker()
        self._model_obj = None

    def load(self):
        if Path(os.path.join(os.getcwd() + MODEL_SAVED_PLACE + "\\" + self._ticker, MODEL_NAME)).is_file():
            self._model_obj = tf.keras.models.load_model(
                os.path.join(os.getcwd() + MODEL_SAVED_PLACE + "\\" + self._ticker, MODEL_NAME))
        else:
            raise FileNotFoundError("the model file is not exist.")

    def predict(self, dataGenerator: StockDataGenerator):
        x_test, _, test_dataset = dataGenerator.generate_future_data()
        y_test = self._model_obj.predict(x_test)
        y_test = np.concatenate([y_test, y_test], axis=1)

        y_test = dataGenerator.get_min_max().inverse_transform(y_test)
        date_arr = np.array(
            [datetime.strftime(timestamp_obj, '%Y-%m-%d')
             for timestamp_obj in test_dataset.index.tolist()][:len(y_test)])

        y_test = y_test[:, 0].reshape(-1, 1)
        date_arr = date_arr.reshape(-1, 1)
        y_test = np.concatenate([date_arr, y_test], axis=1)
        return y_test.tolist()
