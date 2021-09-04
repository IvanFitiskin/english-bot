from aiogram.utils.callback_data import CallbackData

subject_callback = CallbackData('subject', 'subject_name')

translation_to_russian_callback = CallbackData('translation', 'key', 'english', 'page', 'subject')

translation_to_english_callback = CallbackData('english', 'key', 'page', 'subject')


def create_subject_callback(subject_name):
    return subject_callback.new(
        subject_name=subject_name
    )


def create_translation_to_russian_callback(english, page, subject):
    return translation_to_russian_callback.new(
        key='to_russian',
        english=english,
        page=page,
        subject=subject
    )


def create_translation_to_english_callback(page, subject):
    return translation_to_english_callback.new(
        key='to_english',
        page=page,
        subject=subject
    )
