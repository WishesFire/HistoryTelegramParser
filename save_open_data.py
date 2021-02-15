import csv


async def save_messages_to_csv(name, title, temp_history):
    with open(f'E:\\Python3\\TelegramParser\\data\\{name}.csv',
              mode='a', encoding='utf-8') as w_file:
        file_writer = csv.DictWriter(w_file, delimiter=',', lineterminator='\r',
                                     fieldnames=title)
        file_writer.writeheader()
        file_writer.writerows(temp_history)


async def open_message_csv(name):
    with open(f'E:\\Python3\\TelegramParser\\data\\{name}.csv', mode='r', encoding='utf-8') as w_file:
        # TODO функция статистика
        pass