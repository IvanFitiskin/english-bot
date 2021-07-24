import json

from src.models.common import db
from src.models.dictionary import English, Russian, EnglishRussianLink


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
            db.session.flush()
            id_eng = new_eng_word.id
        else:
            id_eng = eng_word_db.id

        for russian_word in russian_words:
            rus_word_db = db.session.query(Russian).filter_by(word=russian_word).first()
            if not rus_word_db:
                new_rus_word = Russian(
                    russian_word
                )
                db.session.add(new_rus_word)
                db.session.flush()
                id_rus = new_rus_word.id
            else:
                id_rus = rus_word_db.id

            eng_rus_link_db = db.session.query(EnglishRussianLink).filter_by(
                id_eng=id_eng,
                id_rus=id_rus
            ).first()
            if not eng_rus_link_db:
                new_eng_rus_link = EnglishRussianLink(
                    id_eng,
                    id_rus
                )
                db.session.add(new_eng_rus_link)
                db.session.flush()

    db.session.commit()

    return
