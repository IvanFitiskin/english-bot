from tgbot.src.keyboards.inline.pagination import get_page_list_keyboard
from tgbot.src.keyboards.inline.subject import create_subject_keyboard


def create_message(word, transcription, page, max_limit):
    text = f'{word} - [{transcription}]'
    markup_pagination = get_page_list_keyboard(max_limit, page)

    markup_keyboard = create_subject_keyboard()
    markup_keyboard.row(*markup_pagination)

    return text, markup_keyboard
