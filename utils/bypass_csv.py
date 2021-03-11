import pandas as pd
import numpy as np
from datetime import datetime


def iter_csv(file):
    data_list = list(file)[1:]
    full_date_list = create_full_date_list(data_list)
    start, finish = data_list[0][2], data_list[-1][2]
    specific_start, specific_finish = start[:10].split('-'), finish[:10].split('-')
    index = generate_empty_date_behind(finish)

    general_date = pd.date_range(start=f'1-1-{finish[2:4]}', end=f'12-31-{start[2:4]}')
    special_date = pd.date_range(start=f'{specific_finish[1]}-{specific_finish[2]}-{specific_finish[0]}',
                                 end=f'{specific_start[1]}-{specific_start[2]}-{specific_start[0]}')
    index = create_data_list(special_date, index, full_date_list)
    index = generate_empty_date_front(index, start)

    print(index)
    print('//////////////////////////')
    print('//////////////////////////')
    print(general_date)
    avg_temp = pd.Series(data=index.astype(float), index=general_date)
    print(avg_temp.head())
    return avg_temp


def generate_empty_date_behind(element):
    date = datetime.strptime(element[:10], '%Y-%m-%d')
    first_day = datetime.strptime(f'{element[:4]}-01-01', '%Y-%m-%d')
    zero_day = (date - first_day).days
    index = np.array([0] * zero_day)
    return index


def generate_empty_date_front(index, start):
    date = datetime.strptime(start[:10], '%Y-%m-%d')
    last_day = datetime.strptime(f'{start[:4]}-12-31', '%Y-%m-%d')
    zero_day = (last_day - date).days
    index = np.append(index, [0] * zero_day)
    return index


def create_full_date_list(data_lst):
    omg = []
    for lst in data_lst:
        try:
            omg.append(lst[2][:10])
        except IndexError:
            continue
    return omg


def create_data_list(count_date, index, full):
    for i in count_date:
        normal = str(i)[:10]
        if normal in full:
            index = np.append(index, full.count(normal))
        else:
            index = np.append(index, 0)

    return index
