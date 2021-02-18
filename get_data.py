from telethon.tl.functions.messages import GetHistoryRequest
from handlers import correspond_user, history_messages
from save_open_data import save_messages_to_csv
import nest_asyncio

nest_asyncio.apply()

the_longest_message = ''
the_most_counted_message = {}

limit_msg = 200
title = ['От кого', 'Сообщения', 'Время']


async def main(client, username):
    global the_longest_message
    async for dialog in client.iter_dialogs():
        offset_msg = 0
        print(dialog.name)
        try:
            if not dialog.entity.bot and dialog.name != '':
                channel = await client.get_entity(dialog.name)
                print(channel)
                while True:
                    chat = await client(GetHistoryRequest(
                                    peer=channel,
                                    limit=200,
                                    offset_date=None,
                                    offset_id=0,
                                    add_offset=offset_msg,
                                    max_id=0,
                                    min_id=0,
                                    hash=0))
                    if not chat.messages:
                        continue
                    temp_history = []
                    try:
                        for message in chat.messages:
                            if 'https://' not in message.message or 'http://' not in message.message:
                                if len(str(message.message)) > len(str(the_longest_message)):
                                    the_longest_message = message.message
                            if message.out:
                                whom_message = 'Я'
                            else:
                                whom_message = dialog.name
                            if message.message == '':
                                message.message = 'image'
                            temp_history.append({title[0]: whom_message, title[1]: message.message, title[2]: message.date})

                        await save_messages_to_csv(dialog.name, title, temp_history)

                        offset_msg += len(chat.messages)
                        if offset_msg >= chat.count:
                            print(offset_msg)
                            the_most_counted_message[dialog.name] = chat.count
                            break
                    except TypeError:
                        continue

        except AttributeError as error:
            print(error)
            continue

    await control_panel()


async def control_panel():
    print('Data collection is complete')
    print(f'The longest message is {the_longest_message}')
    top_3, top_2, top_1 = await correspond_user(the_most_counted_message)
    print('The most correspondent: ')
    print(f'Top 1 {top_1}')
    print(f'Top 2 {top_2}')
    print(f'Top 3 {top_3}')
    await history_messages()
