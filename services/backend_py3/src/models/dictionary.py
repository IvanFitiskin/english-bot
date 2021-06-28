from backend_py3.src.models.common import db


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

    russian_link = db.relationship(
        'Russian', uselist=True, backref='english',
    )

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
    id_eng = db.Column(
        db.Integer,
        db.ForeignKey('english.id')
    )

    def __init__(self, word: str, id_eng: int):
        self.word = word
        self.id_eng = id_eng
