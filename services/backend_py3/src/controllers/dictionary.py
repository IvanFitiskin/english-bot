import connexion
import json
import uuid

from flask import Response, jsonify

from flask import current_app, make_response
from werkzeug.exceptions import BadRequest

from src.models.common import db
from src.models.dictionary import English, Russian, EnglishRussianLink

from src.controllers.const import (
    ENGLISH_GET, ENGLISH_NOT_GET,
    RUSSIAN_GET, RUSSIAN_NOT_GET
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


def get_russian_word(english_word: str) -> Response:
    if not english_word:
        raise BadRequest('Field `english_word` is empty')

    english_russian_query_result = db.session.query(English.id, English.word, Russian.word).join(
        EnglishRussianLink, English.id == EnglishRussianLink.id_eng
    ).join(
        Russian, Russian.id == EnglishRussianLink.id_rus
    ).filter(
        English.word == english_word
    ).all()

    data = {}

    if len(english_russian_query_result) == 0:
        response = make_response(
            jsonify({
                'data': data,
                'message': RUSSIAN_NOT_GET
            }), 404
        )
        return response

    id_eng = 0
    russian_words = []
    for id_eng_db, english_word_db, russian_word_db in english_russian_query_result:
        id_eng = id_eng_db
        russian_words.append(russian_word_db)

    data = {
        'id_eng': id_eng,
        'english': english_word,
        'russian': russian_words
    }
    response = make_response(
        jsonify({
            'data': data,
            'message': RUSSIAN_GET
        }), 200
    )

    return response
