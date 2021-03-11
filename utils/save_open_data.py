import csv
import json
from config import BASEDIR_MAIN, BASEDIR_STAT
from utils.bypass_csv import iter_csv
import pandas as pd

count_message_title = ["Пользователь", "Количество"]


async def save_messages_to_csv(name, title, temp_history):
    with open(f'{BASEDIR_MAIN}\\{name}.csv',
              mode='a', encoding='utf-8') as w_file:
        file_writer = csv.DictWriter(w_file, delimiter=',', lineterminator='\r',
                                     fieldnames=title)
        file_writer.writeheader()
        file_writer.writerows(temp_history)


def open_message_csv(name):
    with open(f'{BASEDIR_MAIN}\\{name}.csv', mode='r', encoding='utf-8') as w_file:
        file_reader = csv.reader(w_file)
        ready_file = iter_csv(file_reader)
    return ready_file


def open_pd_csv(name):
    dm = pd.read_csv(f'{BASEDIR_MAIN}\\{name}.csv', parse_dates=['Время'])
    dm.set_index('date', inplace=True)
    return dm


async def save_static_data(the_longest_message, the_most_counted_message):
    with open(f'{BASEDIR_STAT}\\CountMessage.csv', mode='w', encoding='utf-8') as w_file:
        file_writer = csv.DictWriter(w_file, delimiter=',', lineterminator='\r', fieldnames=count_message_title)
        file_writer.writeheader()
        file_writer.writerows(the_most_counted_message)

    with open(f'{BASEDIR_STAT}\\LongMessage.txt', mode='w', encoding='utf-8') as file:
        file.write(the_longest_message)

    with open(f'{BASEDIR_STAT}\\CountMessage.txt', mode='w', encoding='utf-8') as file:
        file.write(json.dumps(the_most_counted_message))


def open_static_data():
    with open(f'{BASEDIR_STAT}\\CountMessage.txt', mode='r', encoding='utf-8') as file:
        a = file.read()
    return a


def open_static_data_js():
    with open(f'{BASEDIR_STAT}\\CountMessage.txt', mode='r', encoding='utf-8') as file:
        a = json.load(file)
    return a
