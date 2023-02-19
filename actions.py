import requests
import config
from dispatcher import dp, BotDataBase
from aiogram import types
from parse_url import parse_page

keyboard_find = types.ReplyKeyboardMarkup(resize_keyboard=True).row(types.KeyboardButton('/find'))
keyboard_stop = types.ReplyKeyboardMarkup(resize_keyboard=True).row(types.KeyboardButton('/stop'))


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    if not BotDataBase.user_exists(message.from_user.id):
        BotDataBase.add_user(message.from_user.id)
    await message.bot.send_message(message.from_user.id, 'Hi! Enjoy The Music ;p', reply_markup=keyboard_find)


@dp.message_handler(commands='find')
async def begin_search(message: types.Message):
    BotDataBase.toggle_on(message.from_user.id)
    await message.bot.send_message(
        message.from_user.id, 'Enter Name Of The Song, Group Or Author That You Trying To Find! :D',
        reply_markup=keyboard_stop)


@dp.message_handler(commands='stop')
async def stop_search(message):
    BotDataBase.toggle_off(message.from_user.id)
    await message.bot.send_message(message.from_user.id, 'Search Has Been Stopped!', reply_markup=keyboard_find)


@dp.message_handler()
async def find_music(message: types.Message):
    await message.bot.send_message(message.from_user.id, 'Search Has Been Started...', reply_markup=keyboard_stop)
    links = parse_page(config.WEB_PAGE + message.text)
    index = 0
    while index != len(links):
        if not BotDataBase.is_playing(message.from_user.id):
            break
        response = requests.get(links[index]).content
        index += 1
        await message.bot.send_audio(message.from_user.id, response)
