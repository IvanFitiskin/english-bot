import os

from config.secret import SECRET_TG_BOT_TOKEN


class Config(object):
    POSTGRES_HOST = os.getenv('DB_HOST', 'localhost')
    POSTGRES_PORT = os.getenv('DB_PORT', '54320')
    POSTGRES_USER = 'postgres'
    POSTGRES_PW = '12345678'
    POSTGRES_DB = 'english'

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

    RUN_IN_DOCKER = os.getenv('RUN_IN_DOCKER', False)

    # FLASK_CONFIGURATION = 'development'

    if RUN_IN_DOCKER:
        SERVICE_HOST = 'http://englishbot'
    else:
        SERVICE_HOST = 'http://localhost'

    SERVICE_PORT = '5000'
    SERVICE_URL = '{}:{}'.format(
        SERVICE_HOST, SERVICE_PORT,
    )

    if RUN_IN_DOCKER:
        PRODUCTION_DATA_PATH = '/english-bot/data/production/'
    else:
        PRODUCTION_DATA_PATH = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '..',
            'data',
            'production',
            'airport.json',
        )

    TG_BOT_TOKEN = SECRET_TG_BOT_TOKEN
