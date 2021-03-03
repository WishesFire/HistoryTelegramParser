from telethon.tl.functions.messages import GetHistoryRequest
from handlers import correspond_user
from save_open_data import save_messages_to_csv, save_static_data
import nest_asyncio

nest_asyncio.apply()

the_longest_message = ''
the_most_counted_message = {}

limit_msg = 500
title = ['От кого', 'Сообщения', 'Время']


async def main(client):
    global the_longest_message, the_most_counted_message
    async for dialog in client.iter_dialogs():
        offset_msg = 0
        print(f'{dialog.name} is working')
        try:
            if not dialog.entity.bot and dialog.name != '':
                channel = await client.get_entity(dialog.name)
                print(channel)
                while True:
                    chat = await client(GetHistoryRequest(
                                    peer=channel,
                                    limit=limit_msg,
                                    offset_date=None,
                                    offset_id=0,
                                    add_offset=offset_msg,
                                    max_id=0,
                                    min_id=0,
                                    hash=0))
                    if not chat.messages:
                        break
                    temp_history = []
                    try:
                        print('Взяли пачку данных')
                        for message in chat.messages:
                            if not isinstance(message.message, str):
                                continue
                            if 'https://' not in message.message or 'http://' not in message.message:
                                if len(str(message.message)) > len(str(the_longest_message)):
                                    the_longest_message = message.message
                            if message.out:
                                whom_message = 'Я'
                            else:
                                whom_message = dialog.name
                            if message.message == '':
                                message.message = 'image'
                            temp_history.append({title[0]: whom_message, title[1]: message.message,
                                                 title[2]: message.date})

                        await save_messages_to_csv(dialog.name, title, temp_history)

                        offset_msg += len(chat.messages)
                        if offset_msg >= chat.count:
                            print(offset_msg)
                            the_most_counted_message[dialog.name] = chat.count
                            break
                    except TypeError as error:
                        print(error)
                        s = str(error)
                        if s == "'Messages' object has no attribute 'count'":
                            the_most_counted_message[dialog.name] = offset_msg
                        continue

        except AttributeError as error:
            print(error)
            s = str(error)
            if s == "'Messages' object has no attribute 'count'":
                the_most_counted_message[dialog.name] = offset_msg
            continue
        print(f'{dialog.name} finish!!!!')

    await control_panel()


async def control_panel():
    await save_static_data(the_longest_message, the_most_counted_message)
    print('Data collection is complete')
    print(f'The longest message is {the_longest_message}')
    corr = await correspond_user(the_most_counted_message)
    print('The most correspondent: ')
    print(f'Top 1 {corr[-1]}')
    print(f'Top 2 {corr[-2]}')
    print(f'Top 3 {corr[-3]}')
