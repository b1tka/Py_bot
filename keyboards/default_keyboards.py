from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button1 = KeyboardButton('Расписание на сегодня')
button2 = KeyboardButton('/help')
button3 = KeyboardButton('Ссылка на код')
button4 = KeyboardButton('Расписание на завтра')

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(button1).insert(button4).add(button2).insert(button3)
