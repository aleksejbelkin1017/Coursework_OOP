import os
import pytest
from src.filehandler import JSONFileHandler


@pytest.fixture
def json_file_handler(tmp_path):
    """Фикстура для создания временного файла JSON."""
    test_file = tmp_path / "test_vacancies.json"
    handler = JSONFileHandler(str(test_file))
    yield handler
    if os.path.exists(test_file):
        os.remove(test_file)


def test_add_vacancy(json_file_handler):
    vacancy = {
        'id': 1,
        'name': 'Software Engineer',
        'employer': {'name': 'Company A'},
        'alternate_url': 'http://example.com/vacancy/1',
        'salary': {'from': 1000, 'to': 2000}
    }

    json_file_handler.add_vacancy(vacancy)
    vacancies = json_file_handler.get_vacancies()

    assert len(vacancies) == 1
    assert vacancies[0] == vacancy


def test_add_duplicate_vacancy(json_file_handler):
    vacancy = {
        'id': 1,
        'name': 'Software Engineer',
        'employer': {'name': 'Company A'},
        'alternate_url': 'http://example.com/vacancy/1',
        'salary': {'from': 1000, 'to': 2000}
    }

    json_file_handler.add_vacancy(vacancy)
    json_file_handler.add_vacancy(vacancy)
    vacancies = json_file_handler.get_vacancies()

    assert len(vacancies) == 1


def test_get_vacancies_with_criteria(json_file_handler):
    vacancy1 = {
        'id': 1,
        'name': 'Software Engineer',
        'employer': {'name': 'Company A'},
        'alternate_url': 'http://example.com/vacancy/1',
        'salary': {'from': 1000, 'to': 2000}
    }
    vacancy2 = {
        'id': 2,
        'name': 'Data Scientist',
        'employer': {'name': 'Company B'},
        'alternate_url': 'http://example.com/vacancy/2',
        'salary': {'from': 1500, 'to': 2500}
    }

    json_file_handler.add_vacancy(vacancy1)
    json_file_handler.add_vacancy(vacancy2)

    filtered_vacancies = json_file_handler.get_vacancies(name='Data Scientist')

    assert len(filtered_vacancies) == 1
    assert filtered_vacancies[0] == vacancy2


def test_delete_vacancy(json_file_handler):
    vacancy = {
        'id': 1,
        'name': 'Software Engineer',
        'employer': {'name': 'Company A'},
        'alternate_url': 'http://example.com/vacancy/1',
        'salary': {'from': 1000, 'to': 2000}
    }

    json_file_handler.add_vacancy(vacancy)
    json_file_handler.delete_vacancy(1)

    vacancies = json_file_handler.get_vacancies()

    assert len(vacancies) == 0


def test_get_vacancies_empty_file(json_file_handler):
    vacancies = json_file_handler.get_vacancies()
    assert vacancies == []
