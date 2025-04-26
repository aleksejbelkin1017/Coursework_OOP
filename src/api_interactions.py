from abc import ABC, abstractmethod
from typing import Dict, List, Union

import requests


class JobAPI(ABC):
    """
        Абстрактный класс для работы с API вакансий.
    """
    @abstractmethod
    def _connect(self) -> requests.Response:
        """Метод для подключения к API"""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, cantidad: int) -> list:
        """
        Метод для получения вакансий по ключевому слову.

        :param keyword: Ключевое слово для поиска вакансий.
        :param cantidad: Количество вакансий для получения.
        :return: Список вакансий.
        """
        pass


class HH_API(JobAPI):
    """
        Класс для работы с API HeadHunter.
    """
    BASE_URL = "https://api.hh.ru/vacancies"

    def __init__(self) -> None:
        self.__session: Union[requests.Session, None] = None

    def _connect(self) -> requests.Response:
        """
        Метод для подключения к API HeadHunter и получения базового ответа.

        :return: Ответ от сервера.
        """
        self.__session = requests.Session()
        response = self.__session.get(self.BASE_URL)
        response.raise_for_status()
        return response

    def get_vacancies(self, keyword: str, cantidad: int) -> List[Dict]:
        """
        Метод для получения списка вакансий с HeadHunter по заданному ключевому слову и количеству.

        :param keyword: Ключевое слово для поиска вакансий.
        :param cantidad: Количество вакансий для получения.
        :return: Список словарей с вакансиями.
        """
        self._connect()

        params: Dict[str, Union[str, int]] = {
            'text': keyword,
            'per_page': cantidad
        }

        if self.__session is not None:
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
