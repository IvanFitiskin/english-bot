from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from src.keyboards.callback.tools import create_subject_callback,\
    create_translation_to_russian_callback, create_translation_to_english_callback


def create_tools_keyboard(english_word, page):
    markup = InlineKeyboardMarkup(row_width=1)

    subject_button = InlineKeyboardButton(
        text=f'Subject - All words',
        callback_data='dump'
    )

    translation_button = InlineKeyboardButton(
        text='Russian translation \u21bb',
        callback_data=create_translation_to_russian_callback(
            english=english_word,
            page=page,
            subject='All words'
        )
    )

    markup.insert(subject_button)
    markup.insert(translation_button)

    return markup


def create_russian_tools_keyboard(page, subject='All words'):
    markup = InlineKeyboardMarkup(row_width=1)

    translation_button = InlineKeyboardButton(
        text='English translation \u21bb',
        callback_data=create_translation_to_english_callback(
            page=page,
            subject=subject
        )
    )

    markup.insert(translation_button)

    return markup
