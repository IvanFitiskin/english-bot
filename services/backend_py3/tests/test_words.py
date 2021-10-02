import requests
import pytest

from config.backend_py3 import Config

SERVICE_URL = Config.SERVICE_URL


result_1 = {
        "data": [
            {
                "id": 1,
                "transcription": "[ pleɪn ]",
                "word": "plane"
            }
        ],
        "message": "ENGLISH_GET",
        "total_records": 80
    }

result_10 = {
    "data": [
        {
            "id": 10,
            "transcription": "[ 'rʌnwei ]",
            "word": "runway"
        }
    ],
    "message": "ENGLISH_GET",
    "total_records": 80
}

result_80 = {
    "data": [
        {
            "id": 80,
            "transcription": "[ ɪnˈvent ]",
            "word": "to invent"
        }
    ],
    "message": "ENGLISH_GET",
    "total_records": 80
}

result_81 = {
    "data": [{}],
    "message": "ENGLISH_NOT_GET",
    "total_records": 0
}


@pytest.mark.parametrize("page, result", [
    (1, result_1),
    (10, result_10),
    (80, result_80),
    (81, result_81),
])
def test_get_english_word_by_page(page, result):
    response_json = requests.get(f'{SERVICE_URL}/v1/english', params={
        'page': page
    }).json()

    word_data = response_json.get('data')[0]
    test_word_data = result.get('data')[0]

    assert word_data.get('transcription', None) == test_word_data.get('transcription', None)
    assert word_data.get('word', None) == test_word_data.get('word', None)
    assert response_json.get('message', None) == result.get('message', None)
    assert response_json.get('total_records', None) == result.get('total_records', None)


def test_get_english_word_by_page_empty():
    response = requests.get(f'{SERVICE_URL}/v1/english', params={
        'page': 0
    })

    assert response.status_code == 400
    assert response.json().get('detail') == 'Field `page` is empty'
