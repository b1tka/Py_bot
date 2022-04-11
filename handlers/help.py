from aiogram import types, Dispatcher
from shuffling import dp, bot
from keyboards import kb


@dp.message_handler(commands=['start', 'help'])
async def start_with_new_user(message: types.Message):
    await bot.send_message(message.from_user.id, 'Добро пожаловать в теллеграм бота "kar1nocka" \n'
                                                 'Бот создан для проекта\n'
                                                 'Создатель: bitak1f\n'
                                                 'Исходный код: ссылка на github\n', reply_markup=kb)


def register_handler_clients(dp: Dispatcher):
    dp.register_message_handler(start_with_new_user, commands=['start, help'])
