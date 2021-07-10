from aiogram.types import InlineKeyboardButton
from tgbot.src.keyboards.callback.pagination import create_pagination_callback


def get_page_list_keyboard(max_limit: int, page_number=1):
    # Клавиатура будет выглядеть вот так:
    # |<< | <5> | >>|

    previous_page = page_number - 1
    previous_page_text = '\u2190 Назад'

    current_page_text = f'{page_number} из {max_limit}'

    next_page = page_number + 1
    next_page_text = 'Далее \u2192'

    callback_prev_button, callback_next_button = create_pagination_callback(page_number)

    custom_markup = list()
    if previous_page > 0:
        custom_markup.append(
            InlineKeyboardButton(
                text=previous_page_text,
                callback_data=callback_prev_button
            )
        )

    custom_markup.append(
        InlineKeyboardButton(
            text=current_page_text,
            callback_data='current_page'
        )
    )

    if next_page <= max_limit:
        custom_markup.append(
            InlineKeyboardButton(
                text=next_page_text,
                callback_data=callback_next_button
            )
        )

    return custom_markup
