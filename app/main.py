from aiogram import Bot, Dispatcher, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import CallbackQuery

from app.common.keyboard import keyboard_registration
from app.common.keyboard.back import keyboard_changes
from services import TelegramMessageService

bot = Bot(token='7486884923:AAF_tom9VlE6gHPu0yR96xK_kKBpStCHisY', default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await message.answer(text="Привет!", reply_markup=keyboard_registration)

@dp.message()
async def send_cocktail_recipe(message: types.Message) -> None:

    service = TelegramMessageService(message)
    service.processing()

    if message.text == "Отправь рецепт коктейля":
        await message.answer(text="""Вот простой рецепт коктейля Мохито, который легко приготовить!
           Ингридиенты:
           1. 50мл рома
           2. Сок 1 лайма 
           3. 1-2 чайные ложки сахара
           4. 6-8 листиков свежей мяты.
           5. Газированная вода
           7. Газированная вода
           Наслаждайся!
           """)
    elif message.text == "Еще рецепт":
        await message.answer(text="""Рецепт коктейля Маргарита, который тебе понравится!
        Ингредиенты:
        1. 50 мл текилы
        2. 25 мл апельсинового ликера
        3. 25 мл сока лайма
        4. Соль для ободка стакана
        5. Лёд
        Пробуй!
        """)
    else:
        await message.answer(text=message.text)

@dp.callback_query(F.data == 'registration')
async def callback_query_registration(callback_query: CallbackQuery):
    await callback_query.message.answer('Хорошо, приступим ко второму вопросу.')

@dp.callback_query(F.data == 'information')
async def information_about_bot(callback_query: CallbackQuery):
    await callback_query.message.answer(text='Данный бот нужен,чтобы вы смогли быстро найти рецепт коктейля.', reply_markup=keyboard_changes)

@dp.callback_query(F.data == 'back')
async def going_back(callback_query: CallbackQuery):
    await callback_query.message.edit_text(text='Назад')



