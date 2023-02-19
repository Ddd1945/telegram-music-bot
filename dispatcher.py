import logging
import config
from aiogram import Bot, Dispatcher
from data_base import BotDataBase

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

BotDataBase = BotDataBase(config.DATA_BASE)
