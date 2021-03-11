from utils.save_open_data import open_message_csv, open_static_data_js
from handlers.statistics import Graphics


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


def history_messages():
    people_choice = str(input("Choose user, to get statistic: "))
    csv_data = open_message_csv(people_choice)
    Graphics.calendar_heat_map(csv_data)
