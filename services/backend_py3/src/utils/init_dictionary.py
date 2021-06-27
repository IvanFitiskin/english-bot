from backend_py3.src.models.common import db
from backend_py3.src.models.dictionary import English, Russian


def added_new_english_word(word):
    id_word = db.session.query(English).filter_by(word=word).first()
    if not id_word:
        new_word = English(
            word
        )
        db.session.add(new_word)
        db.session.commit()
