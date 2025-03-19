from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu = [
    [InlineKeyboardButton(text='Посмотреть добавленные оценки', callback_data='show_rate')],
    [InlineKeyboardButton(text='Добавить оценку', callback_data='add_rate')]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])