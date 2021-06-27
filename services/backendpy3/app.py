import connexion

from flask_cors import CORS

from backendpy3.models.common import db

app = connexion.App(__name__)
logger = app.app.logger


def create_app():
    print(app.get_root_path())
    app.add_api(
        'swagger.yaml', validate_responses=True, strict_validation=True,
    )
    application = app.app

    application.config.from_object('common.config.Config')

    CORS(application)

    db.init_app(application)
    db.app = application
    db.session.execute('CREATE EXTENSION IF NOT EXISTS pg_trgm;')
    db.session.commit()
    db.create_all()
    db.session.commit()

    return application
