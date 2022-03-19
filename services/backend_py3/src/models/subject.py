from src.models.common import db


class Subject(db.Model):
    """List of topics."""

    __tablename__ = 'subject'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(db.String(80))
    translation = db.Column(db.String(80))

    word = db.relationship("SubjectWordLink", back_populates="subject")

    def __init__(self, name: str, translation: str):
        self.name = name
        self.translation = translation


class SubjectWordLink(db.Model):
    """Link english words with russian words"""

    __tablename__ = 'subject_word_link'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    subject_id = db.Column(
        db.Integer,
        db.ForeignKey('subject.id')
    )
    word_id = db.Column(
        db.Integer,
        db.ForeignKey('word.id')
    )

    subject = db.relationship("Subject", back_populates="word")
    word = db.relationship("Word", back_populates="subject")

    def __init__(self, subject_id: int, word_id: int):
        self.subject_id = subject_id
        self.word_id = word_id
