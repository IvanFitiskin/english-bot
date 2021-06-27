from flask import Response, jsonify


def ping() -> Response:
    return jsonify({})
