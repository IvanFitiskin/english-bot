from flask import Response, jsonify

from flask import make_response
from werkzeug.exceptions import BadRequest

from src.models.common import db
from src.models.dictionary import Word, Translation, WordTranslationLink
from src.models.subject import SubjectWordLink, Subject

from src.controllers.const import (
    WORD_GET, WORD_NOT_GET,
    WORDS_GET, WORDS_NOT_GET,
    TRANSLATION_GET, TRANSLATION_NOT_GET
)


def get_word(page: int) -> Response:
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
                'message': WORD_GET
            }), 200
        )
    else:
        data.append({})
        response = make_response(
            jsonify({
                'data': data,
                'total_records': 0,
                'message': WORD_NOT_GET
            }), 404
        )

    return response


def get_word_by_subject(page: int, subject: str) -> Response:
    if not page:
        raise BadRequest('Field `page` is empty')

    if not subject:
        raise BadRequest('Field `subject` is empty')

    words_from_subject_db = db.session.query(Word.id, Word.name, Subject.name).join(
        SubjectWordLink, SubjectWordLink.word_id == Word.id
    ).join(
        Subject, Subject.id == SubjectWordLink.subject_id
    ).filter(
        Subject.name == subject
    )

    pagination = words_from_subject_db.paginate(
        page=page,
        per_page=20,
        max_per_page=20,
        error_out=False,
    )

    total_records = pagination.total

    data = list()
    for word_id, word_name, subject_name in pagination.items:
        data.append({
            'id': word_id,
            'name': word_name,
            'subject': subject_name
        })

    if len(data) != 0:
        response = make_response(
            jsonify({
                'data': data,
                'total_records': total_records,
                'message': WORDS_GET
            }), 200
        )
    else:
        data.append({})
        response = make_response(
            jsonify({
                'data': data,
                'total_records': 0,
                'message': WORDS_NOT_GET
            }), 404
        )

    return response


def get_translation(word: str) -> Response:
    if not word:
        raise BadRequest('Field `word` is empty')

    word_translation_query_result = db.session.query(Word.id, Word.name, Translation.name).join(
        WordTranslationLink, Word.id == WordTranslationLink.word_id
    ).join(
        Translation, Translation.id == WordTranslationLink.translation_id
    ).filter(
        Word.name == word
    ).all()

    data = {}

    if len(word_translation_query_result) == 0:
        response = make_response(
            jsonify({
                'data': data,
                'message': TRANSLATION_NOT_GET
            }), 404
        )
        return response

    word_id = 0
    translation_names = []
    for word_id_db, word_name_db, translation_name_db in word_translation_query_result:
        word_id = word_id_db
        translation_names.append(translation_name_db)

    data = {
        'word_id': word_id,
        'word': word,
        'translation': translation_names
    }
    response = make_response(
        jsonify({
            'data': data,
            'message': TRANSLATION_GET
        }), 200
    )

    return response
