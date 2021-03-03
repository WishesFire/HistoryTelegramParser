from save_open_data import open_message_csv, open_static_data_js
import asyncio
from statistics import Graphics
import os


async def correspond_user(lst_mess):
    list_sort_mess = list(lst_mess.items())
    list_sort_mess.sort(key=lambda i: i[1])

    return list_sort_mess


def top_1_count(lst_mess):
    list_sort_mess = list(lst_mess.items())
    list_sort_mess.sort(key=lambda i: i[1])

    return list_sort_mess[-1][1]


def correspond_user_statistic():
    list_message = open_static_data_js()
    count_top_1 = top_1_count(list_message)
    Graphics.build_histogram_math(list_message, count_top_1)


def history_messages(flag=None):
    people_choice = str(input("Choose user, to get statistic: "))
    if people_choice in os.listdir('/data_main'):
        csv_data = open_message_csv(people_choice)
        iter_csv_data(csv_data)
        Graphics.calendar_heat_map(csv_data)


async def csv_task(element, data):
    # TODO обходить
    pass


def iter_csv_data(data):
    n_bins = len(data)
    enum = n_bins % 8
    if enum == 0:
        bind = n_bins / 8
    else:
        bind = n_bins // 8

    part_enum = [bind]
    for i in range(8):
        el = bind * 2
        if el >= n_bins:
            break
        elif i == 7 and enum != 0:
            part_enum.append(el + enum)
            break
        part_enum.append(el)

    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(csv_task(e, data)) for e in part_enum]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()