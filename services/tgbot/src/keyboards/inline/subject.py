from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from src.keyboards.callback.subject import create_subject_callback


def create_subject_keyboard(subject='All words'):
    markup = InlineKeyboardMarkup(row_width=1)

    subject_button = InlineKeyboardButton(
        text=subject,
        callback_data='dump'
    )
    markup.insert(subject_button)

    return markup
