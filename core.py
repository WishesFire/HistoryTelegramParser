from telethon import TelegramClient
from handlers.get_data import main
import configparser

# Get config telegram
config = configparser.ConfigParser()
config.read("config.ini")


if __name__ == '__main__':
    api_tg = int(config['Telegram']['api_id'])
    hash_tg = str(config['Telegram']['api_hash'])
    username_tg = str(config['Telegram']['username'])

    client = TelegramClient(username_tg, api_tg, hash_tg)
    client.start()

    try:
        with client:
            client.loop.run_until_complete(main(client))
    except OSError:
        print('Bad connection with main handlers')
