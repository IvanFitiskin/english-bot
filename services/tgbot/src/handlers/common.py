from aiogram import Dispatcher
from aiogram.types import Message

from src.client import BackendClient

client = BackendClient()


async def start_education(message: Message):
    start_message = \
        f'Привет, {message.from_user.full_name}!\nНачнем учить английский? '\
        f'Для запуска первого списка слов воспользуйтесь командой /english'
    await message.answer(start_message)


async def ping(message: Message):
    start_message = f'Просто пинг, для дебагинга бота'
    await message.answer(start_message)


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(start_education, commands=['start'], state="*")


def register_ping_handler(dp: Dispatcher):
    dp.register_message_handler(ping, commands=['ping'], state="*")
