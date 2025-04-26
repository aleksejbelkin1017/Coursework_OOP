from unittest.mock import patch

import pytest

from src.filehandler import JSONFileHandler
from src.vacancies import Vacancy


@pytest.fixture
def mock_session():
    with patch('src.api_interactions.requests.Session') as mock:
        yield mock


@pytest.fixture
def vacancy1():
    return Vacancy(1, 'Python Developer', 'Pupa Company', 100000, "некорректная ссылка")


@pytest.fixture
def vacancy2():
    return Vacancy(2, 'Senior Python Developer', 'Lupa Enterprise', -200000, "http://example.com")


@pytest.fixture
def vacancy3():
    return Vacancy(3, 'SRE engineer', 200000, 200000, "http://example.com")


@pytest.fixture
def vacancy4():
    return Vacancy(4, 123, 'Trulyalya Official', 150000, "http://example.com")


@pytest.fixture
def vacancy5():
    return Vacancy(5, 'Data Analyst', 'Tralyalya Incorporated', 150000, "http://example.com")


@pytest.fixture
def json_file_handler(tmpdir):
    handler = JSONFileHandler(filename=str(tmpdir.join("test_vacancies.json")))
    return handler
