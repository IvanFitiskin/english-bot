from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from src.keyboards.callback.tools import create_subject_callback, create_translation_callback


def create_tools_keyboard(english_word, page, subject='All words'):
    markup = InlineKeyboardMarkup(row_width=1)

    subject_button = InlineKeyboardButton(
        text=f'Subject - {subject}',
        callback_data='dump'
    )

    translation_button = InlineKeyboardButton(
        text='Russian translation \u21bb',
        callback_data=create_translation_callback(
            english_word=english_word,
            page=page,
            subject=subject
        )
    )

    markup.insert(subject_button)
    markup.insert(translation_button)

    return markup
