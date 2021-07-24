from aiogram.utils.callback_data import CallbackData


pagination_callback = CallbackData('paginator', 'key', 'page_number')


def create_pagination_callback(page_number):
    key_prev = 'prev_page'
    key_next = 'next_page'

    callback_prev_button = pagination_callback.new(
        key=key_prev,
        page_number=page_number,
    )
    callback_next_button = pagination_callback.new(
        key=key_next,
        page_number=page_number
    )

    return callback_prev_button, callback_next_button
