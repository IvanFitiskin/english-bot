from src.models.common import db


class Subject(db.Model):
    """List of topics."""

    __tablename__ = 'subject'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    word = db.Column(db.String(80))
    transcription = db.Column(db.String(80))

    english = db.relationship("SubjectEnglishLink", back_populates="subject")

    def __init__(self, word: str, transcription: str):
        self.word = word
        self.transcription = transcription


class SubjectEnglishLink(db.Model):
    """Link english words with russian words"""

    __tablename__ = 'subject_english_link'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    subject_id = db.Column(
        db.Integer,
        db.ForeignKey('subject.id')
    )
    english_id = db.Column(
        db.Integer,
        db.ForeignKey('english.id')
    )

    subject = db.relationship("Subject", back_populates="english")
    english = db.relationship("English", back_populates="subject")

    def __init__(self, subject_id: int, english_id: int):
        self.subject_id = subject_id
        self.english_id = english_id
