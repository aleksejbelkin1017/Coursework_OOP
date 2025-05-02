from src.vacancies import Vacancy


def test_valid_vacancy(vacancy5: Vacancy) -> None:
    """
    Тестирует валидную вакансию с корректными значениями всех полей.

    Args:
        vacancy5: Объект вакансии с корректными данными
    """
    assert vacancy5.name == "Data Analyst"
    assert vacancy5.company == "Tralyalya Incorporated"
    assert vacancy5.salary == 150000
    assert vacancy5.url == "http://example.com"


def test_invalid_name(vacancy4: Vacancy) -> None:
    """
    Тестирует вакансию с некорректным (пустым) названием.

    Args:
        vacancy4: Объект вакансии с пустым названием
    """
    assert vacancy4.name == "Название вакансии не указано"


def test_invalid_company(vacancy3: Vacancy) -> None:
    """
    Тестирует вакансию с некорректным (пустым) названием компании.

    Args:
        vacancy3: Объект вакансии с пустым названием компании
    """
    assert vacancy3.company == "Название компании-работодателя не указано"


def test_invalid_salary(vacancy2: Vacancy) -> None:
    """
    Тестирует вакансию с некорректной (нулевой) зарплатой.

    Args:
        vacancy2: Объект вакансии с нулевой зарплатой
    """
    assert vacancy2.salary == 0


def test_invalid_url(vacancy1: Vacancy) -> None:
    """
    Тестирует вакансию с некорректной (пустой) ссылкой.

    Args:
        vacancy1: Объект вакансии с пустой ссылкой
    """
    assert vacancy1.url == "Ссылка не указана"


def test_salary_comparison(vacancy1: Vacancy, vacancy4: Vacancy, vacancy5: Vacancy) -> None:
    """
    Тестирует корректность сравнения вакансий по зарплате.

    Args:
        vacancy1: Вакансия с нулевой зарплатой
        vacancy4: Вакансия с некорректной зарплатой
        vacancy5: Вакансия с корректной зарплатой
    """
    assert vacancy1 < vacancy4
    assert vacancy1 <= vacancy4
    assert vacancy4 > vacancy1
    assert vacancy4 >= vacancy1
    assert not (vacancy1 == vacancy4)
    assert vacancy4 == vacancy5
