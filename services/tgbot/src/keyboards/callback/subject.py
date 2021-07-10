from aiogram.utils.callback_data import CallbackData

subject_callback = CallbackData('subject', 'subject_name')


def create_subject_callback(subject_name):
    subject_callback_button = subject_callback.new(
        subject_name=subject_name
    )

    return subject_callback_button
