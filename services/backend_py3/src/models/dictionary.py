from src.models.common import db


class English(db.Model):
    """List of english words."""

    __tablename__ = 'english'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    word = db.Column(db.String(80))
    transcription = db.Column(db.String(80))

    russian = db.relationship("EnglishRussianLink", back_populates="english")
    subject = db.relationship("SubjectEnglishLink", back_populates="english")

    def __init__(self, word: str, transcription: str):
        self.word = word
        self.transcription = transcription


class Russian(db.Model):
    """List of russian words."""

    __tablename__ = 'russian'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    word = db.Column(db.String(80))

    english = db.relationship("EnglishRussianLink", back_populates="russian")

    def __init__(self, word: str):
        self.word = word


class EnglishRussianLink(db.Model):
    """Link english words with russian words"""

    __tablename__ = 'english_russian_link'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    id_eng = db.Column(
        db.Integer,
        db.ForeignKey('english.id')
    )
    id_rus = db.Column(
        db.Integer,
        db.ForeignKey('russian.id')
    )

    english = db.relationship("English", back_populates="russian")
    russian = db.relationship("Russian", back_populates="english")

    def __init__(self, id_eng: int, id_rus: int):
        self.id_eng = id_eng
        self.id_rus = id_rus
