import logging
from aiogram import Dispatcher

from aiogram.types import CallbackQuery, ParseMode, Message
from src.client import BackendClient

from src.message.english_content_message import create_message
from src.keyboards.callback.pagination import pagination_callback

client = BackendClient()


async def print_first_english_word(message: Message):
    data = {
        'page': 1
    }
    response_json = client.get_english_word(data)
    logging.info(f'{response_json}')
    max_limit = response_json.get('total_records', None)

    word_data = response_json['data'][0]

    word = word_data.get('word')
    transcription = word_data.get('transcription')

    text, markup_keyboard = create_message(word, transcription, 1, max_limit)

    await message.answer(
        text=text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=markup_keyboard
    )


async def print_prev_english_word(call: CallbackQuery, callback_data: dict):
    prev_page = int(callback_data.get('page_number')) - 1

    data = {
        'page': prev_page
    }
    response_json = client.get_english_word(data)
    max_limit = response_json.get('total_records', None)

    word_data = response_json['data'][0]

    word = word_data.get('word')
    transcription = word_data.get('transcription')

    text, markup_keyboard = create_message(word, transcription, prev_page, max_limit)

    await call.message.edit_text(
        text=text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=markup_keyboard
    )


async def print_next_english_word(call: CallbackQuery, callback_data: dict):
    next_page = int(callback_data.get('page_number')) + 1

    data = {
        'page': next_page
    }
    response_json = client.get_english_word(data)
    max_limit = response_json.get('total_records', None)

    word_data = response_json['data'][0]

    word = word_data.get('word')
    transcription = word_data.get('transcription')

    text, markup_keyboard = create_message(word, transcription, next_page, max_limit)

    await call.message.edit_text(
        text=text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=markup_keyboard
    )


def register_card_handlers(dp: Dispatcher):
    dp.register_message_handler(print_first_english_word, commands=['english'], state="*")
    dp.register_callback_query_handler(print_prev_english_word,
                                       pagination_callback.filter(key='prev_page'))
    dp.register_callback_query_handler(print_next_english_word,
                                       pagination_callback.filter(key='next_page'))
