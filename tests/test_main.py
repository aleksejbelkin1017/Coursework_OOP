import os
from pathlib import Path
from typing import Generator

import pytest

from src.filehandler import JSONFileHandler


@pytest.fixture
def json_file_handler(tmp_path: Path) -> Generator[JSONFileHandler, None, None]:
    """
    Фикстура для создания временного файла JSON.
    Создает временный файл для хранения вакансий и удаляет его после теста.
    """
    test_file = tmp_path / "test_vacancies.json"
    handler = JSONFileHandler(str(test_file))
    yield handler
    if os.path.exists(test_file):
        os.remove(test_file)


def test_add_vacancy(json_file_handler: JSONFileHandler) -> None:
    """
        Тест добавления одной вакансии.

        Проверяет:
        - Добавление новой вакансии
        - Корректность сохранения данных
        - Количество вакансий после добавления
    """
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


def test_add_duplicate_vacancy(json_file_handler: JSONFileHandler) -> None:
    """
        Тест добавления дублирующейся вакансии.

        Проверяет:
        - Игнорирование дубликатов при добавлении
        - Количество уникальных вакансий
    """
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


def test_get_vacancies_with_criteria(json_file_handler: JSONFileHandler) -> None:
    """
        Тест фильтрации вакансий по критериям.

        Проверяет:
        - Корректность фильтрации по имени
        - Возвращаемый результат фильтрации
    """
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


def test_delete_vacancy(json_file_handler: JSONFileHandler) -> None:
    """
        Тест удаления вакансии.

        Проверяет:
        - Корректность удаления по ID
        - Отсутствие удаленной вакансии в списке
    """
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


def test_get_vacancies_empty_file(json_file_handler: JSONFileHandler) -> None:
    """
        Тест проверяет корректность обработки пустого JSON файла.

        Проверяемое поведение:
        - При попытке получить вакансии из пустого файла
        - Метод должен вернуть пустой список

        Параметры:
        json_file_handler (JsonFileHandler): экземпляр класса-обработчика JSON файла

        Ожидаемый результат:
        Метод get_vacancies() должен вернуть пустой список вакансий []
    """
    vacancies = json_file_handler.get_vacancies()
    assert vacancies == []
