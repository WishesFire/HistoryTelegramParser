from telethon.tl.functions.messages import GetHistoryRequest
import nest_asyncio
import csv

nest_asyncio.apply()

the_longest_message = ''
count_message = {}

limit_msg = 200
title = ['От кого', 'Сообщения', 'Время']


async def main(client, username):
    global the_longest_message
    audit = True
    while audit:
        choice = int(input('What task do you want? '))
        if isinstance(choice, int) and choice < 5:
            audit = False
            async for dialog in client.iter_dialogs():
                offset_msg = 0
                print(dialog)
                try:
                    if not dialog.entity.bot and dialog.name != '':
                        channel = await client.get_entity(dialog.name)
                        print(channel)
                        chat = await client(GetHistoryRequest(
                                peer=channel,
                                limit=0,
                                offset_date=None,
                                offset_id=0,
                                add_offset=offset_msg,
                                max_id=0,
                                min_id=0,
                                hash=0))
                        if not chat.messages:
                            continue
                        temp_history = []
                        for message in chat.messages:
                            if 'https://' not in message.message or 'http://' not in message.message:
                                if len(str(message.message)) > len(str(the_longest_message)):
                                    the_longest_message = message.message
                            if message.out:
                                whom_message = 'Я'
                            else:
                                whom_message = dialog.name
                            temp_history.append({title[0]: whom_message, title[1]: message.message,
                                                 title[2]: message.date})

                        with open(f'data/{dialog.name}', mode='w', encoding='utf-8') as w_file:
                            file_writer = csv.DictWriter(w_file, delimiter=',', lineterminator='\r', fieldnames=title)
                            file_writer.writeheader()
                            file_writer.writerows(temp_history)

                        offset_msg += len(chat.messages)
                        if offset_msg % 1000 == 0:
                            print(offset_msg)

                except AttributeError as error:
                    print(error)
                    continue
