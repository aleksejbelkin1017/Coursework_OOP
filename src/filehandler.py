from abc import ABC, abstractmethod
import json
import os


class FileHandler(ABC):
    def __init__(self, filename):
        self.__filename = filename

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, **criteria):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id):
        pass


class JSONFileHandler(FileHandler):
    def __init__(self, filename="Data/vacancies.json"):
        super().__init__(filename)

    def add_vacancy(self, vacancy):
        """Метод для добавления вакансии в файл"""
        vacancies = self.get_vacancies()
        if vacancy not in vacancies:
            vacancies.append(vacancy)
            with open(self._FileHandler__filename, 'w') as f:
                json.dump(vacancies, f, indent=4)

    def get_vacancies(self, **criteria):
        """Метод для получения вакансии по указанным критериям"""
        if not os.path.exists(self._FileHandler__filename):
            return []
        with open(self._FileHandler__filename, 'r') as f:
            vacancies = json.load(f)
        if criteria:
            filtered_vacancies = []
            for vacancy in vacancies:
                if all(vacancy.get(key) == value for key, value in criteria.items()):
                    filtered_vacancies.append(vacancy)
            return filtered_vacancies
        return vacancies

    def delete_vacancy(self, vacancy_id):
        """Метод для удаления вакансии"""
        vacancies = self.get_vacancies()
        vacancies = [vacancy for vacancy in vacancies if vacancy.get('id') != vacancy_id]
        with open(self._FileHandler__filename, 'w') as f:
            json.dump(vacancies, f, indent=4)
