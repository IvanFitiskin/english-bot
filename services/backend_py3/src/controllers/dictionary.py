import connexion
import json
import uuid

from flask import Response, jsonify

from flask import current_app, make_response
from werkzeug.exceptions import BadRequest

from backend_py3.src.models.common import db
from backend_py3.src.models.dictionary import English

from backend_py3.src.controllers.const import (
    ENGLISH_GET, ENGLISH_NOT_GET
)


def get_english_words(page: int) -> Response:
    if not page:
        raise BadRequest('Field `page` is empty')

    words_db = db.session.query(English)

    pagination = words_db.paginate(
        page=page,
        per_page=1,
        max_per_page=50,
        error_out=False,
    )

    total_records = pagination.total

    data = []
    for english in pagination.items:
        transcription = english.transcription
        data.append({
            'id': english.id,
            'word': english.word,
            'transcription': transcription
        })

    if len(data) != 0:
        response = make_response(
            jsonify({
                'data': data,
                'total_records': total_records,
                'message': ENGLISH_GET
            }), 200
        )
    else:
        response = make_response(
            jsonify({
                'data': data,
                'total_records': 0,
                'message': ENGLISH_NOT_GET
            }), 404
        )

    return response
