import json

from src.models.common import db
from src.models.dictionary import English, Russian, EnglishRussianLink
from src.models.subject import Subject, SubjectEnglishLink


def create_topic_base(subject_name, subject_translation):
    subject_db = db.session.query(Subject).filter_by(word=subject_name).first()
    if not subject_db:
        new_subject_db = Subject(
            subject_name,
            subject_translation
        )
        db.session.add(new_subject_db)
        db.session.flush()
        subject_id = new_subject_db.id
    else:
        subject_id = subject_db.id

    db.session.commit()

    return subject_id


def create_dictionary(path):
    with open(path, 'r') as f:
        data = json.loads(f.read())

    subject = data.get('subject', None)

    subject_name = subject.get('english', None)
    subject_translation = subject.get('russian', None)
    subject_id = create_topic_base(subject_name, subject_translation)

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

        sub_eng_link_db = db.session.query(SubjectEnglishLink).filter_by(
            subject_id=subject_id,
            english_id=id_eng
        ).first()
        if not sub_eng_link_db:
            new_sub_eng_link_db = SubjectEnglishLink(
                subject_id,
                id_eng
            )
            db.session.add(new_sub_eng_link_db)
            db.session.flush()

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
