from telethon import TelegramClient
from config import *
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


Turtle = TelegramClient('Turtle', APP_ID, API_HASH).start(bot_token=BOT_TOKEN) 