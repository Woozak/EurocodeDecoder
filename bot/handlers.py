from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.utils import decode_eurocode


router = Router()


@router.message(Command(commands=['start']))
async def start_command(message: Message):
    welcome_message = (f'👋 Привет!\n'
                       f'Я бот для расшифровки еврокодов автомобильных стекол.\n'
                       f'Введите еврокод, чтобы получить информацию о стекле.')
    await message.answer(text=welcome_message)


@router.message()
async def any_message(message: Message):
    await message.answer(text=decode_eurocode(message.text))
