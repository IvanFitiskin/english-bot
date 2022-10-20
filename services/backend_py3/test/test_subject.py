import requests
import pytest

from config.backend_py3 import Config

SERVICE_URL = Config.SERVICE_URL

TEST_CASES = [
    ({
        "data": [
            {
                "id": 1,
                "name": "airport",
                "translation": "аэропорт"
            },
            {
                "id": 2,
                "name": "furniture",
                "translation": "мебель"
            },
            {
                "id": 3,
                "name": "Homework autumn 3",
                "translation": "Домашняя работа, осень №3"
            },
            {
                "id": 4,
                "name": "lesson-1",
                "translation": "Мой урок №1"
            },
            {
                "id": 5,
                "name": "lesson-2",
                "translation": "Мой урок №2"
            },
            {
                "id": 6,
                "name": "profession",
                "translation": "Профессия"
            }
        ],
        "message": "SUBJECT_GET"
    })
]


@pytest.mark.parametrize("result", TEST_CASES)
def test_get_english_word_by_page(result):
    response = requests.get(f'{SERVICE_URL}/v1/subject')

    print(response.json())

    #assert response.status_code == 200
    assert response.json() == result
