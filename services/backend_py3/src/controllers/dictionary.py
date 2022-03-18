import connexion
import json
import uuid

from flask import Response, jsonify

from flask import current_app, make_response
from werkzeug.exceptions import BadRequest

from src.models.common import db
from src.models.dictionary import Word, Russian, WordRussianLink

from src.controllers.const import (
    ENGLISH_GET, ENGLISH_NOT_GET,
    RUSSIAN_GET, RUSSIAN_NOT_GET
)


def get_english_words(page: int) -> Response:
    if not page:
        raise BadRequest('Field `page` is empty')

    words_db = db.session.query(Word)

    pagination = words_db.paginate(
        page=page,
        per_page=1,
        max_per_page=50,
        error_out=False,
    )

    total_records = pagination.total

    data = list()
    for word in pagination.items:
        transcription = word.transcription
        data.append({
            'id': word.id,
            'name': word.name,
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
        data.append({})
        response = make_response(
            jsonify({
                'data': data,
                'total_records': 0,
                'message': ENGLISH_NOT_GET
            }), 404
        )

    return response


def get_russian_word(word: str) -> Response:
    if not word:
        raise BadRequest('Field `english_word` is empty')

    word_russian_query_result = db.session.query(Word.id, Word.name, Russian.word).join(
        WordRussianLink, Word.id == WordRussianLink.word_id
    ).join(
        Russian, Russian.id == WordRussianLink.id_rus
    ).filter(
        Word.name == word
    ).all()

    data = {}

    if len(word_russian_query_result) == 0:
        response = make_response(
            jsonify({
                'data': data,
                'message': RUSSIAN_NOT_GET
            }), 404
        )
        return response

    word_id = 0
    russian_words = []
    for word_id_db, word_name_db, russian_word_db in word_russian_query_result:
        word_id = word_id_db
        russian_words.append(russian_word_db)

    data = {
        'word_id': word_id,
        'word': word,
        'russian': russian_words
    }
    response = make_response(
        jsonify({
            'data': data,
            'message': RUSSIAN_GET
        }), 200
    )

    return response
