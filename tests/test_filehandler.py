def test_add_vacancy(json_file_handler, vacancy1):
    json_file_handler.add_vacancy(vacancy1.to_dict())

    # Проверяем, что вакансия добавлена
    vacancies = json_file_handler.get_vacancies()
    assert len(vacancies) == 1
    assert vacancies[0]['id'] == 1


def test_add_duplicate_vacancy(json_file_handler, vacancy1):
    json_file_handler.add_vacancy(vacancy1.to_dict())
    json_file_handler.add_vacancy(vacancy1.to_dict())  # Добавляем дубликат

    # Проверяем, что дубликат не добавился
    vacancies = json_file_handler.get_vacancies()
    assert len(vacancies) == 1


def test_add_notduplicate(json_file_handler, vacancy1, vacancy2):
    json_file_handler.add_vacancy(vacancy1.to_dict())
    json_file_handler.add_vacancy(vacancy2.to_dict())
    vacancies = json_file_handler.get_vacancies()
    assert len(vacancies) == 2


def test_get_vacancies_by_criteria(json_file_handler, vacancy1, vacancy2):
    json_file_handler.add_vacancy(vacancy1.to_dict())
    json_file_handler.add_vacancy(vacancy2.to_dict())

    # Проверяем фильтрацию по критериям
    filtered_vacancies = json_file_handler.get_vacancies(company="Pupa Company")
    assert len(filtered_vacancies) == 1
    assert filtered_vacancies[0]['id'] == 1


def test_delete_vacancy(json_file_handler, vacancy1):
    json_file_handler.add_vacancy(vacancy1.to_dict())
    json_file_handler.delete_vacancy(1)
    vacancies = json_file_handler.get_vacancies()
    assert len(vacancies) == 0
