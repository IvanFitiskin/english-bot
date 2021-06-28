import json

from backend_py3.src.models.common import db
from backend_py3.src.models.dictionary import English, Russian


def create_dictionary(path):
    with open(path, 'r') as f:
        data = json.loads(f.read())

    words = data.get('words', None)

    if not words:
        return

    for word in words:
        english_word = word.get('english', None)
        transcription = word.get('transcription', None)
        russian_words = word.get('russian', None)

        eng_word_db = db.session.query(English).filter_by(word=english_word).first()
        if not eng_word_db:
            new_eng_word = English(
                english_word,
                transcription
            )
            db.session.add(new_eng_word)

        for russian_word in russian_words:
            rus_word_db = db.session.query(Russian).filter_by(word=russian_word).first()
            if not rus_word_db:
                eng_word_for_russian = db.session.query(English).filter_by(word=english_word).first()
                new_rus_word = Russian(
                    russian_word,
                    eng_word_for_russian.id
                )
                db.session.add(new_rus_word)

    db.session.commit()

    return
