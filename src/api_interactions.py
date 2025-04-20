from abc import ABC, abstractmethod
import requests


class JobAPI(ABC):
    @abstractmethod
    def _connect(self):
        """Метод для подключения к API"""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, cantidad: int):
        """Метод для получения вакансий по ключевому слову"""
        pass


class hh_API(JobAPI):
    BASE_URL = "https://api.hh.ru/vacancies"

    def __init__(self):
        self.__session = None

    def _connect(self):
        """Метод для подключения к API"""
        self.__session = requests.Session()
        response = self.__session.get(self.BASE_URL)
        response.raise_for_status()
        return response

    def get_vacancies(self, keyword: str, cantidad: int):
        """Метод для получения вакансий по ключевому слову"""
        self._connect()

        params = {
            'text': keyword,
            'per_page': cantidad
        }

        response = self.__session.get(self.BASE_URL, params=params)
        response.raise_for_status()

        vacancies = response.json().get('items', [])
        return [
            {
                'name': vacancy['name'],
                'company': vacancy['employer']['name'],
                'url': vacancy['alternate_url'],
                'salary': vacancy.get('salary'),
                'id': vacancy.get('id')
            }
            for vacancy in vacancies
        ]
