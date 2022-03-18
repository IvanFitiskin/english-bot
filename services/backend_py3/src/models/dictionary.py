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

    russian = db.relationship("WordRussianLink", back_populates="word")
    subject = db.relationship("SubjectWordLink", back_populates="word")

    def __init__(self, name: str, transcription: str):
        self.name = name
        self.transcription = transcription


class Russian(db.Model):
    """List of russian words."""

    __tablename__ = 'russian'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(db.String(80))

    word = db.relationship("WordRussianLink", back_populates="russian")

    def __init__(self, name: str):
        self.name = name


class WordRussianLink(db.Model):
    """Link english words with russian words"""

    __tablename__ = 'word_russian_link'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    word_id = db.Column(
        db.Integer,
        db.ForeignKey('word.id')
    )
    id_rus = db.Column(
        db.Integer,
        db.ForeignKey('russian.id')
    )

    word = db.relationship("Word", back_populates="russian")
    russian = db.relationship("Russian", back_populates="word")

    def __init__(self, word_id: int, id_rus: int):
        self.word_id = word_id
        self.id_rus = id_rus
