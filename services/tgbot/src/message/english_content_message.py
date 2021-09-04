from src.keyboards.inline.pagination import get_page_list_keyboard
from src.keyboards.inline.tools import create_tools_keyboard


def create_message(word, transcription, page, max_limit):
    text = f'{word} - [{transcription}]'
    markup_pagination = get_page_list_keyboard(max_limit, page)

    markup_keyboard = create_tools_keyboard(word, page)
    markup_keyboard.row(*markup_pagination)

    return text, markup_keyboard
