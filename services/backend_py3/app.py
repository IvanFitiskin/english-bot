import connexion
import os

from flask_cors import CORS

from src.models.common import db
from src.utils.init_dictionary import create_dictionary

app = connexion.App(__name__)
logger = app.app.logger


def create_app():
    app.add_api(
        'swagger.yaml', validate_responses=True, strict_validation=True,
    )
    application = app.app

    application.config.from_object('config.backend_py3.Config')

    CORS(application)

    db.init_app(application)
    db.app = application
    db.session.execute('CREATE EXTENSION IF NOT EXISTS pg_trgm;')
    db.session.commit()
    db.create_all()
    db.session.commit()

    PRODUCTION_DATA_PATH = application.config.get('PRODUCTION_DATA_PATH')

    for root, dirs, files in os.walk(PRODUCTION_DATA_PATH):
        for filename in files:
            path = os.path.join(PRODUCTION_DATA_PATH, filename)
            create_dictionary(path)

    return application
