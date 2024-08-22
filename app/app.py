from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart, Command
from aiogram.types.input_file import FSInputFile

from commands.friday import CommandFriday

bot = Bot(token='7486884923:AAF_tom9VlE6gHPu0yR96xK_kKBpStCHisY', default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await message.answer("Привет!")

@dp.message(CommandFriday())
async def command_start_handler(message: types.Message) -> None:
    await message.answer("Сегодня пятница!")

@dp.message(Command('hi', prefix='$'))
async def command_start_handler(message: types.Message) -> None:
    await message.answer("За деньги да!")

@dp.message()
async def message_handler(message: types.Message) -> None:
    if message.voice:
        await message.answer(text='Я не хочу разговаривать.')
    elif message.photo:
        file = FSInputFile('photo/00.png')
        await message.reply_photo(file)
    await message.answer(text=message.text)
