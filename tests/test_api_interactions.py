from unittest.mock import Mock
from src.api_interactions import hh_API


def test_get_vacancies(mock_session):
    hh_api_exemple = hh_API()

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

    vacancies = hh_api_exemple.get_vacancies("Python", 10)

    assert len(vacancies) == 2
    assert vacancies[0]['name'] == 'Python Developer'
    assert vacancies[0]['salary'] == {'from': 1000, 'to': 2000}
    assert vacancies[0]['company'] == 'Pupa Company'
    assert vacancies[1]['name'] == 'Senior Python Developer'
    assert vacancies[1]['salary'] is None
    assert vacancies[1]['company'] == 'Lupa Enterprise'


def test_get_vacancies_no_vacancies(mock_session):
    hh_api_exemple = hh_API()

    mock_response = Mock()
    mock_response.json.return_value = {
        'items': []
    }
    mock_response.raise_for_status = Mock()
    mock_session.return_value.get.return_value = mock_response

    vacancies = hh_api_exemple.get_vacancies("Python", 10)

    assert len(vacancies) == 0
