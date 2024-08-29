from aiogram import types
import os
from typing import TextIO


class TelegramMessageService:
    def __init__(self, message: types.Message):
        self.message = message
        self.user_telegram_id = message.chat.id

    def processing(self):
        file = self._get_or_create_user_file()
        self._write_data(file, self.message.text)
        self._close_file(file)

    def _get_or_create_user_file(self) -> TextIO:
        file_path = f"./db/{self.user_telegram_id}.txt"
        if os.path.exists(file_path):
            f = open(file_path, 'a', encoding='utf-8' )
        else:
            f = open(file_path, 'w', encoding='utf-8')
        return f

    def _write_data(self, file: TextIO, text):
        file.write(text + '\n')

    def _close_file(self, file):
        file.close()
