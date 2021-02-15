from datetime import datetime
from save_open_data import open_message_csv
import os


async def correspond_user(lst_mess):
    #TODO функция статистика
    list_sort_mess = list(lst_mess.items())
    list_sort_mess.sort(key=lambda i: i[1])


async def history_messages():
    people_choice = str(input("Choose user, to get statistic: "))
    if people_choice in os.listdir('E:\\Python3\\TelegramParser\\data'):
        await open_message_csv(people_choice)


async def online_message():
    pass
