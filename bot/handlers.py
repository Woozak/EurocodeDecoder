from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.utils import decode_eurocode


router = Router()


@router.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer('')


@router.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer('')


@router.message()
async def any_message(message: Message):
    await message.answer(text=decode_eurocode(message.text))
