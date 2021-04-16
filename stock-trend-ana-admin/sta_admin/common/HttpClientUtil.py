__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '2021/4/12 21:27'

from datetime import datetime

import requests
from FileUtil import save_record_2_file
import json
import os

DATA_SAVED_PLACE = "\index"


def record_get_request(url, result_file_path):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}

    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text)['data'][0]['attributes']
        row = {
            "values": {"name": datetime.now().strftime("%H:%M:%S"), "value": data['last']},
            "percentChange": data['percentChange'],
            "change": round(data['change'], 2),
            "latestVal": round(data['last'], 2)
        }
        save_record_2_file(os.path.join(os.getcwd() + DATA_SAVED_PLACE, result_file_path), row)
    else:
        print('something wrong with crontab task, since ：%s' % response.status_code)


def send_get_request(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.text)['data'][0]['attributes']
        return {
            "latestVal": round(data['last'], 2)
        }
    else:
        print('something wrong with crontab task, since ：%s' % response.status_code)
        return {
            "latestVal": 0
        }
