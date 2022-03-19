import json

from src.models.common import db
from src.models.dictionary import Word, Translation, WordTranslationLink
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
        translation_words = word.get('russian', None)

        word_db = db.session.query(Word).filter_by(name=word_name).first()
        if not word_db:
            new_word_db = Word(
                word_name,
                transcription
            )
            db.session.add(new_word_db)
            db.session.flush()
            word_id = new_word_db.id
        else:
            word_id = word_db.id

        sub_word_link_db = db.session.query(SubjectWordLink).filter_by(
            subject_id=subject_id,
            word_id=word_id
        ).first()
        if not sub_word_link_db:
            new_sub_word_link_db = SubjectWordLink(
                subject_id,
                word_id
            )
            db.session.add(new_sub_word_link_db)
            db.session.flush()

        for translation_name in translation_words:
            translation_name_db = db.session.query(Translation).filter_by(name=translation_name).first()
            if not translation_name_db:
                new_translation_name_db = Translation(
                    translation_name
                )
                db.session.add(new_translation_name_db)
                db.session.flush()
                translation_id = new_translation_name_db.id
            else:
                translation_id = translation_name_db.id

            word_translation_link_db = db.session.query(WordTranslationLink).filter_by(
                word_id=word_id,
                translation_id=translation_id
            ).first()
            if not word_translation_link_db:
                new_word_translation_link_db = WordTranslationLink(
                    word_id,
                    translation_id
                )
                db.session.add(new_word_translation_link_db)
                db.session.flush()

    db.session.commit()

    return
