from src.models.common import db


class Word(db.Model):
    """List of words."""

    __tablename__ = 'word'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(db.String(80))
    transcription = db.Column(db.String(80))

    translation = db.relationship("WordTranslationLink", back_populates="word")
    subject = db.relationship("SubjectWordLink", back_populates="word")

    def __init__(self, name: str, transcription: str):
        self.name = name
        self.transcription = transcription


class Translation(db.Model):
    """List of translation words."""

    __tablename__ = 'translation'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(db.String(80))

    word = db.relationship("WordTranslationLink", back_populates="translation")

    def __init__(self, name: str):
        self.name = name


class WordTranslationLink(db.Model):
    """Link english words with russian words"""

    __tablename__ = 'word_translation_link'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    word_id = db.Column(
        db.Integer,
        db.ForeignKey('word.id')
    )
    translation_id = db.Column(
        db.Integer,
        db.ForeignKey('translation.id')
    )

    word = db.relationship("Word", back_populates="translation")
    translation = db.relationship("Translation", back_populates="word")

    def __init__(self, word_id: int, translation_id: int):
        self.word_id = word_id
        self.translation_id = translation_id
