import requests
import pytest

from config.backend_py3 import Config

SERVICE_URL = Config.SERVICE_URL

TEST_CASES = [
    (1, {
        "data": [
            {
                "id": 1,
                "transcription": "[ pleɪn ]",
                "name": "plane"
            }
        ],
        "message": "WORD_GET",
        "total_records": 81
    }),
    (10, {
        "data": [
            {
                "id": 10,
                "transcription": "[ 'rʌnwei ]",
                "name": "runway"
            }
        ],
        "message": "WORD_GET",
        "total_records": 81
    }),
    (80, {
        "data": [
            {
                "id": 80,
                "transcription": "[ ɪnˈvent ]",
                "name": "to invent"
            }
        ],
        "message": "WORD_GET",
        "total_records": 81
    }),
    (81, {
        "data": [
            {
                "id": 81,
                "transcription": "[ ˈfɪʃəmən ]",
                "name": "fisherman"
            }
        ],
        "message": "WORD_GET",
        "total_records": 81
    })
]


@pytest.mark.parametrize("page, result", TEST_CASES)
def test_get_english_word_by_page(page, result):
    response = requests.get(f'{SERVICE_URL}/v1/word', params={
        'page': page
    })

    assert response.status_code == 200
    assert response.json() == result


def test_get_english_word_by_page_empty():
    response = requests.get(f'{SERVICE_URL}/v1/word', params={
        'page': 0
    })

    assert response.status_code == 400
    assert response.json().get('detail') == 'Field `page` is empty'
