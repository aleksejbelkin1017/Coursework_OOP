from typing import Dict, List, Optional
from unittest.mock import Mock

from src.api_interactions import HH_API


def test_get_vacancies(mock_session: Mock) -> None:
    """
    Тест получения вакансий с проверкой корректности данных

    Проверяет:
    - Количество полученных вакансий
    - Корректность заполнения полей каждой вакансии
    - Обработку вакансий с разной структурой зарплаты
    """
    hh_api_exemple = HH_API()

    mock_response = Mock()
    mock_response.json.return_value = {
        'items': [
            {
                'name': 'Python Developer',
                'alternate_url': 'https://example.com/vacancy/1',
                'salary': {'from': 1000, 'to': 2000},
                'employer': {'name': 'Pupa Company', 'id': 1}
            },
            {
                'name': 'Senior Python Developer',
                'alternate_url': 'https://example.com/vacancy/2',
                'salary': None,
                'employer': {'name': 'Lupa Enterprise', 'id': 2}
            }
        ]
    }
    mock_response.raise_for_status = Mock()
    mock_session.return_value.get.return_value = mock_response

    vacancies: List[Dict[str, Optional[Dict[str, int]]]] = hh_api_exemple.get_vacancies("Python", 10)

    assert len(vacancies) == 2
    assert vacancies[0]['name'] == 'Python Developer'
    assert vacancies[0]['salary'] == {'from': 1000, 'to': 2000}
    assert vacancies[0]['company'] == 'Pupa Company'
    assert vacancies[1]['name'] == 'Senior Python Developer'
    assert vacancies[1]['salary'] is None
    assert vacancies[1]['company'] == 'Lupa Enterprise'


def test_get_vacancies_no_vacancies(mock_session: Mock) -> None:
    """
    Тест получения пустого списка вакансий

    Проверяет:
    - Обработку случая отсутствия вакансий
    - Корректное возвращение пустого списка
    """
    hh_api_exemple = HH_API()

    mock_response = Mock()
    mock_response.json.return_value = {
        'items': []
    }
    mock_response.raise_for_status = Mock()
    mock_session.return_value.get.return_value = mock_response

    vacancies: List[Dict] = hh_api_exemple.get_vacancies("Python", 10)

    assert len(vacancies) == 0
