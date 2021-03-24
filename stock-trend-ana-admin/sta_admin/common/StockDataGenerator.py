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

    def get_stock_short_name(self):
        return self._ticker.info['shortName']

    def get_min_max(self):
        return self._min_max

    def get_y_min_max(self):
        return self._y_min_max

    def get_stock_currency(self):
        return self._ticker.info['currency']

    def download_basic_info(self):
        if Path(os.path.join(self._stock.get_data_folder(), self._data_save_file)).is_file():
            # if the file exist already
            data = pd.read_csv(os.path.join(self._stock.get_data_folder(), self._data_save_file))
            return data.values.tolist()
        else:
            # if not exist, then download
            end_date = datetime.today()
            try:
                data = yf.download([self._stock.get_ticker()], start=self._stock.get_start_date(), end=end_date)[
                    ['Open', 'Close', 'Low', 'High', 'Volume']]
                data.to_csv(os.path.join(self._stock.get_data_folder(), self._data_save_file))
                return data.values.tolist()
            except TimeoutError:
                print("Download Data Failed, Since the network reason.")
            except:
                print("Download Data Failed. Since some unknown reason.")
            return []

    def download_transform_to_numpy(self, time_steps, project_folder):
        end_date = datetime.today()
        print('End Date: ' + end_date.strftime("%Y-%m-%d"))
        data = yf.download([self._stock.get_ticker()], start=self._stock.get_start_date(), end=end_date)[
            ['Open', 'Close']]
        data = data.reset_index()
        data.to_csv(os.path.join(project_folder, 'downloaded_data_' + self._stock.get_ticker() + '.csv'))
        # print(data)

        training_data = data[data['Date'] < self._stock.get_validation_date()].copy()
        test_data = data[data['Date'] >= self._stock.get_validation_date()].copy()
        training_data = training_data.set_index('Date')
        # Set the data frame index using column Date
        test_data = test_data.set_index('Date')

        train_scaled = self._min_max.fit_transform(training_data)
        # self.__data_verification(train_scaled)

        # Training Data Transformation
        x_train = []
        y_train = []
        for i in range(time_steps, train_scaled.shape[0]):
            # 他用历史前三天的数据预测 第四天的数据
            x_train.append(train_scaled[i - time_steps:i])
            # close price 一定要放在最后
            y_train.append(train_scaled[i, -1])

        x_train, y_train = np.array(x_train), np.array(y_train)
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], -1))

        # 他只是把之前三天拼到了 test_data 上， 比如预测2020-01-01 就需要2019-12-29 2019-12-30 2019-12-31
        total_data = pd.concat((training_data, test_data), axis=0)
        inputs = total_data[len(total_data) - len(test_data) - time_steps:]
        test_scaled = self._min_max.fit_transform(inputs)

        # Testing Data Transformation
        x_test = []
        y_test = []
        for i in range(time_steps, test_scaled.shape[0]):
            x_test.append(test_scaled[i - time_steps:i])
            y_test.append(test_scaled[i, -1])

        x_test, y_test = np.array(x_test), np.array(y_test)
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], -1))
        return (x_train, y_train), (x_test, y_test), (training_data, test_data)

    def __date_range(self, start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)

    def negative_positive_random(self):
        return 1 if random.random() < 0.5 else -1

    def pseudo_random(self):
        return random.uniform(0.01, 0.03)

    def generate_future_data(self, time_steps, min_max, start_date, end_date, latest_close_price):
        # 没有开盘价， 以及其他相关feature？
        x_future = []
        y_future = []

        # We need to provide a randomisation algorithm for the close price
        # This is my own implementation and it will provide a variation of the
        # close price for a +-1-3% of the original value, when the value wants to go below
        # zero, it will be forced to go up.

        original_price = latest_close_price

        for single_date in self.__date_range(start_date, end_date):
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

        test_scaled = min_max.fit_transform(test_data)
        x_test = []
        y_test = []
        # print(test_scaled.shape[0])
        for i in range(time_steps, test_scaled.shape[0]):
            x_test.append(test_scaled[i - time_steps:i])
            y_test.append(test_scaled[i, -1])
            # print(i - time_steps)

        x_test, y_test = np.array(x_test), np.array(y_test)
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], -1))
        return x_test, y_test, test_data
