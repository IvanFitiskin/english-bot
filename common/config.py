import os


class Config(object):
    POSTGRES_HOST = os.getenv('DB_HOST', 'localhost')
    POSTGRES_PORT = os.getenv('DB_PORT', '54320')
    POSTGRES_USER = 'postgres'
    POSTGRES_PW = '12345678'
    POSTGRES_DB = 'postgres'

    SQLALCHEMY_DATABASE_URI = (
        'postgresql+psycopg2:'
        '//{user}:{pw}@{url}:{port}/{db}'.format(
            user=POSTGRES_USER,
            pw=POSTGRES_PW,
            url=POSTGRES_HOST,
            port=POSTGRES_PORT,
            db=POSTGRES_DB,
        )
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False