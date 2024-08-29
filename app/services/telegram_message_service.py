from aiogram import types


class TelegramMessageService:
    def __init__(self, message: types.Message):
        self.message = message
        self.user_telegram_id = message.chat.id

    def processing(self):
        file = self._get_or_create_user_file()
        self._write_data(file, self.message.text)
        self._close_file(file)

    def _get_or_create_user_file(self) -> open:
        pass

    def _write_data(self, file, text):
        pass

    def _close_file(self, file):
        pass
