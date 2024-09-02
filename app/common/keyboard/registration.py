from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

first_row_buttons = [
    InlineKeyboardButton(text='Регистарция', callback_data='registration'),
]
keyboard_registration = InlineKeyboardMarkup(inline_keyboard=[first_row_buttons])
