from Parse_file import Parse
from aiogram import types, Dispatcher
from shuffling import bot, dp
from config import username, password
import datetime as dt
from keyboards import kb


@dp.message_handler()
async def start_parsing(message: types.Message):
    if message.text == 'Расписание на сегодня':
        await bot.send_message(message.from_user.id, 'Пару секунд...')
        user = Parse(username, password, dt.datetime.today().weekday() + 1)
        await bot.send_message(message.from_user.id, user.schedule())
    elif message.text == 'Расписание на завтра':
        await bot.send_message(message.from_user.id, 'Пару секунд...')
        user = Parse(username, password, dt.datetime.today().weekday() + 2)
        await bot.send_message(message.from_user.id, user.schedule())
    elif message.text == 'Ссылка на код':
        await bot.send_message(message.from_user.id, 'Link to code')
    else:
        await bot.send_message(message.from_user.id, 'Выбери пожалуйста вариант из клавиатуры >-<',
                               reply_markup=kb)


def register_handler_clients(dp: Dispatcher):
    dp.register_message_handler(start_parsing)
