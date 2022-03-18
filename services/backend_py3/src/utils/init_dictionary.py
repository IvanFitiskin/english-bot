import json

from src.models.common import db
from src.models.dictionary import Word, Russian, WordRussianLink
from src.models.subject import Subject, SubjectWordLink


def create_topic_base(subject_name, subject_translation):
    subject_db = db.session.query(Subject).filter_by(name=subject_name).first()
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
        word_name = word.get('english', None)
        transcription = word.get('transcription', None)
        russian_words = word.get('russian', None)

        eng_word_db = db.session.query(Word).filter_by(name=word_name).first()
        if not eng_word_db:
            new_word = Word(
                word_name,
                transcription
            )
            db.session.add(new_word)
            db.session.flush()
            word_id = new_word.id
        else:
            word_id = eng_word_db.id

        sub_eng_link_db = db.session.query(SubjectWordLink).filter_by(
            subject_id=subject_id,
            word_id=word_id
        ).first()
        if not sub_eng_link_db:
            new_sub_word_link_db = SubjectWordLink(
                subject_id,
                word_id
            )
            db.session.add(new_sub_word_link_db)
            db.session.flush()

        for russian_word in russian_words:
            rus_word_db = db.session.query(Russian).filter_by(name=russian_word).first()
            if not rus_word_db:
                new_rus_word = Russian(
                    russian_word
                )
                db.session.add(new_rus_word)
                db.session.flush()
                id_rus = new_rus_word.id
            else:
                id_rus = rus_word_db.id

            word_rus_link_db = db.session.query(WordRussianLink).filter_by(
                word_id=word_id,
                id_rus=id_rus
            ).first()
            if not word_rus_link_db:
                new_word_rus_link = WordRussianLink(
                    word_id,
                    id_rus
                )
                db.session.add(new_word_rus_link)
                db.session.flush()

    db.session.commit()

    return
