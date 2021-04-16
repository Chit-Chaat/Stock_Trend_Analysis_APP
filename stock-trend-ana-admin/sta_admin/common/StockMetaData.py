__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '3/23/2021 1:58 AM'

import os
from datetime import datetime

from StringUtil import check_is_subset

DATA_SAVED_PLACE = "/data"


class StockMetaData:
    def __init__(self, ticker, start_date, validation_date="2020-06-01"):
        self._ticker = ticker
        self._start_date = start_date
        self._validation_date = validation_date
        # create or not , make a decision here.
        TOKEN = ticker + '_' + start_date.strftime("%Y%m%d") + '_' + datetime.today().strftime("%Y%m%d")
        AVAILABLE_TOKEN = check_is_subset(TOKEN, os.getcwd() + DATA_SAVED_PLACE)
        if AVAILABLE_TOKEN is None:
            os.makedirs(os.path.join(os.getcwd() + DATA_SAVED_PLACE, TOKEN))
            self._data_folder = os.path.join(os.getcwd() + DATA_SAVED_PLACE, TOKEN)
        else:
            self._data_folder = os.path.join(os.getcwd() + DATA_SAVED_PLACE, AVAILABLE_TOKEN)

    def get_ticker(self):
        return self._ticker

    def set_ticker(self, value):
        self._ticker = value

    def get_start_date(self):
        return self._start_date

    def set_start_date(self, value):
        self._start_date = value

    def get_validation_date(self):
        return self._validation_date

    def set_validation_date(self, value):
        self._validation_date = value

    def get_data_folder(self):
        return self._data_folder

    def set_data_folder(self, value):
        self._data_folder = value
