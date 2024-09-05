from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

click_back = [
    InlineKeyboardButton(text='Назад', callback_data='back')
]
keyboard_changes: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[click_back])
