import json
import os
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Union


class FileHandler(ABC):
    """Абстрактный класс для работы с вакансиями"""
    @abstractmethod
    def add_vacancy(self, vacancy: Dict) -> None:
        """Абстрактный метод для добавления вакансии в файл"""
        pass

    @abstractmethod
    def get_vacancies(self, **criteria: str) -> List[Dict]:
        """Абстрактный метод для получения вакансии по указанным критериям"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id: str) -> None:
        """Абстрактный метод для удаления вакансии"""
        pass


class JSONFileHandler(FileHandler):
    """Класс для работы с вакансиями"""
    def __init__(self, filename: str = "Data/vacancies.json"):
        super().__init__()
        self.__filename = filename

    def add_vacancy(self, vacancy: Dict) -> None:
        """Метод для добавления вакансии в файл"""
        vacancies = self.get_vacancies()
        if vacancy not in vacancies:
            vacancies.append(vacancy)
            with open(self.__filename, 'w') as f:
                json.dump(vacancies, f, indent=4)

    def get_vacancies(self, **criteria: str) -> List[Dict]:
        """Метод для получения вакансии по указанным критериям"""
        if not os.path.exists(self.__filename):
            return []
        with open(self.__filename, 'r') as f:
            vacancies: List[Dict[str, Any]] = json.load(f)
        if criteria:
            filtered_vacancies = []
            for vacancy in vacancies:
                if all(vacancy.get(key) == value for key, value in criteria.items()):
                    filtered_vacancies.append(vacancy)
            return filtered_vacancies
        return vacancies

    def delete_vacancy(self, vacancy_id: Union[str, int]) -> None:
        """Метод для удаления вакансии"""
        vacancies = self.get_vacancies()
        vacancies = [vacancy for vacancy in vacancies if vacancy.get('id') != vacancy_id]
        with open(self.__filename, 'w') as f:
            json.dump(vacancies, f, indent=4)
