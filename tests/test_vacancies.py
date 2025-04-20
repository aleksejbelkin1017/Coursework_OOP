def test_valid_vacancy(vacancy5):
    assert vacancy5.name == "Data Analyst"
    assert vacancy5.company == "Tralyalya Incorporated"
    assert vacancy5.salary == 150000
    assert vacancy5.url == "http://example.com"


def test_invalid_name(vacancy4):
    assert vacancy4.name == "Название вакансии не указано"


def test_invalid_company(vacancy3):
    assert vacancy3.company == "Название компании-работодателя не указано"


def test_invalid_salary(vacancy2):
    assert vacancy2.salary == 0


def test_invalid_url(vacancy1):
    assert vacancy1.url == "Ссылка не указана"


def test_salary_comparison(vacancy1, vacancy4, vacancy5):
    assert vacancy1 < vacancy4
    assert vacancy1 <= vacancy4
    assert vacancy4 > vacancy1
    assert vacancy4 >= vacancy1
    assert not (vacancy1 == vacancy4)
    assert vacancy4 == vacancy5
