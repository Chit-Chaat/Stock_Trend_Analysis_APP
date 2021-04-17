__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '3/23/2021 3:16 AM'

import os
from collections import defaultdict


def check_is_subset(token, token_file_dir, flag=False):
    token_files = os.listdir(token_file_dir)
    if token in token_files:
        # if token exist
        return token
    else:
        # if not exist, check is subset
        if flag:
            t_ticker, t_start, t_end = token.split("_")
            dir_dict = defaultdict(list)
            for file in token_files:
                f_ticker, f_start, f_end = file.split("_")
                dir_dict[f_ticker].append([f_start, f_end])

            if t_ticker not in dir_dict:
                return None
            else:
                available_slots = dir_dict[t_ticker]
                for a_start, a_end in available_slots:
                    # if [a_start [t_start, t_end] a_end]
                    if a_start <= t_start and t_end <= a_end:
                        return t_ticker + '_' + a_start + '_' + a_end

                return None
        else:
            return None

