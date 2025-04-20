import pytest
import requests
from unittest.mock import patch, Mock
from src.head_hunter_api import HeadHunterAPI


# Создаем фикстуру для инициализации объекта
@pytest.fixture
def api_instance():
    api = HeadHunterAPI()
    api.__api_url = 'https://api.example.com'
    api.__headers = {'Authorization': 'token'}
    api.__params = {'page': 1}
    api.__vacancies = []
    return api


def test_successful_connection(api_instance, monkeypatch):
    # Создаем мок-ответ
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'items': ['vacancy1', 'vacancy2']}

    # Заменяем requests.get на мок
    monkeypatch.setattr(requests, 'get', lambda *args, **kwargs: mock_response)

    # Вызываем тестируемый метод
    api_instance._connect_to_api('python', 1)

    # Проверяем результаты
    assert api_instance._HeadHunterAPI__vacancies == ['vacancy1', 'vacancy2']


# Тест с несколькими страницами
def test_multiple_pages(api_instance, monkeypatch):
    # Создаем мок-ответы для двух страниц
    mock_response1 = Mock()
    mock_response1.status_code = 200
    mock_response1.json.return_value = {'items': ['vacancy1', 'vacancy2']}

    mock_response2 = Mock()
    mock_response2.status_code = 200
    mock_response2.json.return_value = {'items': ['vacancy3', 'vacancy4']}

    # Изменяем логику мок-объекта
    monkeypatch.setattr(requests, 'get', lambda *args, **kwargs:
        mock_response1 if kwargs['params']['page'] == 0  # Важно: страницы начинаются с 0
        else mock_response2)

    # Вызываем тестируемый метод
    api_instance._connect_to_api('python', 2)

    # Проверяем результаты
    assert api_instance._HeadHunterAPI__vacancies == ['vacancy1', 'vacancy2', 'vacancy3', 'vacancy4']


# Тест обработки HTTP-ошибки
def test_http_error(api_instance, monkeypatch):
    mock_response = Mock()
    mock_response.status_code = 404
    # Добавляем настройку метода json()
    mock_response.json.side_effect = ValueError("Ошибка API")
    monkeypatch.setattr(requests, 'get', lambda *args, **kwargs: mock_response)

    # Проверяем вывод сообщения об ошибке
    with pytest.raises(Exception, match='Ошибка API'):
        api_instance._connect_to_api('python', 1)


# Тест обработки сетевой ошибки
def test_network_error(api_instance, monkeypatch):
    # Создаем мок-объект с правильным side_effect
    mock_get = Mock(side_effect=requests.exceptions.RequestException('Network error'))
    monkeypatch.setattr(requests, 'get', mock_get)

    # Проверяем вывод сообщения об ошибке
    with pytest.raises(Exception, match='Сетевая ошибка'):
        api_instance._connect_to_api('python', 1)


# Тест пустого ответа
def test_empty_response(api_instance, monkeypatch):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'items': []}
    monkeypatch.setattr(requests, 'get', lambda *args, **kwargs: mock_response)

    api_instance._connect_to_api('python', 1)
    assert api_instance.__vacancies == []


@pytest.fixture
def hh_api():
    return HeadHunterAPI()

@pytest.mark.parametrize("keyword, pages, expected_result", [
    ("python", 1, {"vacancies": ["vacancy1", "vacancy2"]}),
    ("java", 2, {"vacancies": ["java1", "java2", "java3"]}),
    ("", 1, {"vacancies": []}),
    ("python", 0, {"vacancies": []})
])
def test_get_vacancies(hh_api, keyword, pages, expected_result):
    # Мокируем метод _connect_to_api
    with patch.object(hh_api, '_connect_to_api') as mock_connect:
        # Обновляем приватное поле напрямую
        hh_api._HeadHunterAPI__vacancies = expected_result["vacancies"]
        mock_connect.return_value = expected_result

        # Вызываем тестируемый метод
        result = hh_api.get_vacancies(keyword, pages)

        # Проверяем, что метод _connect_to_api был вызван с правильными параметрами
        mock_connect.assert_called_once_with(keyword, pages)

        # Проверяем результат
        assert result == expected_result["vacancies"]

def test_get_vacancies_empty_response(hh_api):
    with patch.object(hh_api, '_connect_to_api') as mock_connect:
        mock_connect.return_value = {"vacancies": []}
        hh_api._HeadHunterAPI__vacancies = []

        result = hh_api.get_vacancies("non_existing_keyword", 1)
        assert result == []

def test_get_vacancies_api_error(hh_api):
    with patch.object(hh_api, '_connect_to_api') as mock_connect:
        mock_connect.side_effect = Exception("API error")

        with pytest.raises(Exception):
            hh_api.get_vacancies("python", 1)
