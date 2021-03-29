__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '3/23/2021 2:56 AM'

import os
from pathlib import Path
import numpy as np
from datetime import timedelta
import random
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime
import yfinance as yf


class StockDataGenerator:
    def __init__(self, stock):
        self._stock = stock
        self._ticker = yf.Ticker(self._stock.get_ticker())
        self._min_max = MinMaxScaler(feature_range=(0, 1))
        self._y_min_max = MinMaxScaler(feature_range=(0, 1))
        self._data_save_file = "data.csv"

    def get_min_max(self):
        return self._min_max

    def get_y_min_max(self):
        return self._y_min_max

    def download_basic_info(self):
        if Path(os.path.join(self._stock.get_data_folder(), self._data_save_file)).is_file():
            # if the file exist already
            rawdata = pd.read_csv(os.path.join(self._stock.get_data_folder(), self._data_save_file))
            data = rawdata[rawdata['Date'] >= self._stock.get_start_date().strftime("%Y-%m-%d")].copy()
            return rawdata, data.values.tolist()
        else:
            # if not exist, then download
            end_date = datetime.today()
            rawdata = None
            try:
                rawdata = yf.download([self._stock.get_ticker()], start=self._stock.get_start_date(), end=end_date)[
                    ['Open', 'Close', 'Low', 'High', 'Volume']]
                rawdata.reset_index(inplace=True)
                data = rawdata[rawdata['Date'] > self._stock.get_start_date().strftime("%Y-%m-%d")].copy()
                data.to_csv(os.path.join(self._stock.get_data_folder(), self._data_save_file))
                data['Date'] = data['Date'].astype(str)
                return data, data.values.tolist()
            except TimeoutError:
                print("Download Data Failed, Since the network reason.")
            except ConnectionError:
                print("Download Data Failed, Since the network reason.")
            except KeyError:
                rawdata.to_csv(os.path.join(self._stock.get_data_folder(), self._data_save_file))
                return rawdata, rawdata.values.tolist()
            except Exception:
                print("Download Data Failed, Since some unknown reason.")
                return [], []
            return [], []

    def __date_range(self, start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)

    def negative_positive_random(self):
        return 1 if random.random() < 0.5 else -1

    def pseudo_random(self):
        return random.uniform(0.01, 0.03)

    def get_time_steps(self):
        self._time_steps = 3
        return self._time_steps

    def generate_future_data(self, neg_or_pos=1):
        # min_max, start_date, end_date, latest_close_price
        # 没有开盘价， 以及其他相关feature？

        data, _ = self.download_basic_info()
        training_data = data[data['Date'] < self._stock.get_validation_date()].copy()
        test_data = data[data['Date'] >= self._stock.get_validation_date()].copy()
        training_data = training_data.set_index('Date')
        # Set the data frame index using column Date
        test_data = test_data.set_index('Date')
        self._min_max.fit_transform(training_data)

        latest_close_price = test_data.Close.iloc[-1]
        latest_date_obj = test_data[-1:]['Close'].idxmin()

        if isinstance(latest_date_obj, str):
            latest_date = datetime.strptime(test_data[-1:]['Close'].idxmin(), '%Y-%m-%d')
        else:
            latest_date = latest_date_obj

        tomorrow_date = latest_date + timedelta(1)
        prediction_end_date = latest_date + timedelta(self.get_time_steps() * 100)

        x_future = []
        y_future = []

        # We need to provide a randomisation algorithm for the close price
        # This is my own implementation and it will provide a variation of the
        # close price for a +-1-3% of the original value, when the value wants to go below
        # zero, it will be forced to go up.

        original_price = latest_close_price

        for single_date in self.__date_range(tomorrow_date, prediction_end_date):
            x_future.append(single_date)
            direction = self.negative_positive_random()
            random_slope = direction * (self.pseudo_random())
            # print(random_slope)
            original_price = original_price + (original_price * random_slope)
            # print(original_price)
            if original_price < 0:
                original_price = 0
            y_future.append(original_price)

        # 这里加了一个Open feature
        test_data = pd.DataFrame({'Date': x_future, 'Close': y_future, 'Open': y_future})
        test_data = test_data.set_index('Date')

        test_scaled = self.get_min_max().fit_transform(test_data)
        x_test = []
        y_test = []

        for i in range(self.get_time_steps(), test_scaled.shape[0]):
            x_test.append(test_scaled[i - self.get_time_steps():i])
            y_test.append(test_scaled[i, -1])

        x_test, y_test = np.array(x_test), np.array(y_test)
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], -1))
        return x_test, y_test, test_data
