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


@router.message(Command(commands=['help']))
async def help_command(message: Message):
    help_message = (f'Еврокод - это код, который содержит информацию о стекле: '
                    f'его тип, марку и модель автомобиля, тип кузова и другие характеристики.\n'
                    f'Чтобы использовать бот, просто отправьте еврокод автомобильного стекла.\n'
                    f'Например: 8340AGNBLV.\n'
                    f'Бот вернёт информацию о стекле, если еврокод будет распознан.\n')
    await message.answer(text=help_message)


@router.message()
async def message_handler(message: Message):
    await message.answer(text=decode_eurocode(message.text))
