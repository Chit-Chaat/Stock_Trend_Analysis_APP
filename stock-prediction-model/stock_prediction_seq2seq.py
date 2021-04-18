import os
import tensorflow as tf
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Dropout, Dense, LSTM

from RealMSE import RealMSE
from ScaledRealMSE import ScaledRealMSE


class LongShortTermMemory:
    def __init__(self, project_folder):
        self.project_folder = project_folder

    def get_defined_metrics(self):
        defined_metrics = [
            tf.keras.metrics.MeanSquaredError(name='MSE'),
            tf.keras.metrics.RootMeanSquaredError(name="RMSE"),
            RealMSE(name="realMSE"),
            ScaledRealMSE(name="scaled_realMSE")
        ]
        return defined_metrics

    def get_callback(self):
        callback = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3, mode='min', verbose=1)
        return callback

    def create_model(self, x_train):
        model = Sequential()
        model.add(LSTM(units=256, return_sequences=True, input_shape=(x_train.shape[1], x_train.shape[2])))
        model.add(Dropout(0.2))
        model.add(LSTM(units=128, return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(units=64, return_sequences=True))
        model.add(Dropout(0.5))
        model.add(LSTM(units=64))
        model.add(Dropout(0.5))
        model.add(Dense(units=1))
        model.summary()
        tf.keras.utils.plot_model(model,
                                  to_file=os.path.join(self.project_folder, 'model_lstm.png'),
                                  show_shapes=True,
                                  show_layer_names=True)
        return model
