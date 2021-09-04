from aiogram.utils.callback_data import CallbackData

subject_callback = CallbackData('subject', 'subject_name')

translation_to_russian_callback = CallbackData('translation', 'english', 'page', 'subject')

translation_to_english_callback = CallbackData('english', 'page', 'subject')


def create_subject_callback(subject_name):
    return subject_callback.new(
        subject_name=subject_name
    )


def create_translation_to_russian_callback(english_word, page, subject):
    return translation_to_russian_callback.new(
        english=english_word,
        page=page,
        subject=subject
    )


def create_translation_to_english_callback(page, subject):
    return translation_to_english_callback.new(
        page=page,
        subject=subject
    )
