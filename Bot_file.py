from aiogram import executor
from shuffling import dp


async def starting_bot(_):
    print('Кариночка работает')


from handlers import help, start_parsing, other

help.start_with_new_user(dp)
start_parsing.start_parsing(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=starting_bot)
