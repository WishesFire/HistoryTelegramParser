from save_open_data import open_message_csv
from statistics import create_histogram_mat
import os


async def correspond_user(lst_mess):
    #TODO функция статистика
    list_sort_mess = list(lst_mess.items())
    list_sort_mess.sort(key=lambda i: i[1])
    create_histogram_mat(list_sort_mess)

    return list_sort_mess


async def history_messages():
    people_choice = str(input("Choose user, to get statistic: "))
    if people_choice in os.listdir('E:\\Python3\\TelegramParser\\data'):
        await open_message_csv(people_choice)


async def online_message():
    # TODO писать всем кто будет в сети
    pass
