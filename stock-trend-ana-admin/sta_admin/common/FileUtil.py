__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '2021/4/12 21:08'

import csv
import json
import os

DATA_SAVED_PLACE = "\index"


def save_record_2_file(file_path, content, mode="a+"):
    if mode == "a+":
        with open(file_path, mode=mode, newline="") as output_file:
            output_file.writelines(json.dumps(content))
            output_file.write("\n")
            output_file.close()
    else:
        pass


def read_txt_file(ticker):
    file_path = ""
    if ticker == "COMP":
        file_path = os.path.join(os.getcwd() + DATA_SAVED_PLACE, 'COMP_index.txt')
    elif ticker == "SP500":
        file_path = os.path.join(os.getcwd() + DATA_SAVED_PLACE, 'SP500_index.txt')
    else:
        return None

    temp_res, result = [], {'values': []}
    with open(file_path, 'r', encoding='utf-8') as data_file:
        lines = data_file.readlines()
        temp_res = lines[-30:]
        data_file.close()

    for line in temp_res:
        json_line = json.loads(line)
        result['values'].append(json_line['values'])

    last_line = json.loads(temp_res[-1])
    result['percentChange'] = last_line['percentChange']
    result['change'] = last_line['change']
    result['latestVal'] = last_line['latestVal']

    return result
