import pytest
from mock import get_weather

def test_get_weather_success(mocker):
    mock_get = mocker.patch('mock.requests.get')
    # Создаем мок-ответ для успешного запроса
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
       'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.15}}
    api_key = 'test_api_key'
    city = 'London'