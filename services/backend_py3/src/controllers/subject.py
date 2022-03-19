from flask import Response, jsonify
from flask import make_response

from src.models.common import db
from src.models.subject import Subject

from src.controllers.const import SUBJECT_GET, SUBJECT_NULL


def get_subject() -> Response:
    subject_db = db.session.query(Subject).all()

    data = list()
    for subject in subject_db:
        data.append({
            'id': subject.id,
            'name': subject.name,
            'translation': subject.translation
        })

    if len(data) != 0:
        response = make_response(
            jsonify({
                'data': data,
                'message': SUBJECT_GET
            }), 200
        )
    else:
        data.append({})
        response = make_response(
            jsonify({
                'data': data,
                'message': SUBJECT_NULL
            }), 404
        )

    return response
