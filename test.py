import pytest
from unittest.mock import patch
from mok import get_cat_image
from config import CATS_API

def test_get_cat_image_success(mocker):
    # Создаем мок-ответ для успешного запроса
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{
        "breed_id": "abys",
        "name": "Abyssinian"
    }]

    # Мокируем requests.get
    mocker.patch('requests.get', return_value=mock_response)

    # Вызываем функцию с тестовыми данными
    breed_id = "abys"
    headers = {"x-api-key": CATS_API}
    cat_data = get_cat_image(breed_id, headers)

    # Проверяем результат
    assert cat_data == [{
        "breed_id": "abys",
        "name": "Abyssinian"
    }]

def test_get_cat_image_error(mocker):
    # Создаем мок-ответ для ошибки
    mock_response = mocker.Mock()
    mock_response.status_code = 404

    # Мокируем requests.get
    mocker.patch('requests.get', return_value=mock_response)

    # Вызываем функцию с тестовыми данными
    breed_id = "abys"
    headers = {"x-api-key": CATS_API}
    cat_data = get_cat_image(breed_id, headers)

    # Проверяем результат
    assert cat_data is None
