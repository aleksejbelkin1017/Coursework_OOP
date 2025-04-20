from abc import ABC, abstractmethod
import requests
from requests.exceptions import HTTPError


class BaseHeadHunterAPI(ABC):
    """
    Абстрактный класс для работы с API hh.ru
    """

    @abstractmethod
    def _connect_to_api(self, keyword: str) -> None:
        """
        Подключается к API hh.ru и сохраняет вакансии в список
        :param keyword: Ключевое слово для поиска вакансий
        :return: None
        """
    @abstractmethod
    def get_vacancies(self, keyword: str) -> list:
        """
        Возвращает список собранных вакансий при помощи API
        :param keyword: Ключевое слово для поиска
        :return: Список словарей с вакансиями
        """


class HeadHunterAPI(BaseHeadHunterAPI):
    def __init__(self):
        self.__api_url = "https://api.hh.ru/vacancies"
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []

    def _connect_to_api(self, keyword, pages: int = 1):
        self.__params['text'] = keyword
        try:
            while self.__params.get('page') != pages:
                response = requests.get(self.__api_url, headers=self.__headers, params=self.__params)
                response.raise_for_status()
                vacancies = response.json().get('items', '')
                self.__vacancies.extend(vacancies)
                self.__params['page'] += 1
        except HTTPError as e:
            print(f"Ошибка API: {e}")
            return None
        except requests.exceptions.RequestException as e:
            raise Exception('Сетевая ошибка') from e


    def get_vacancies(self, keyword, pages: int = 1):
        self._connect_to_api(keyword, pages)
        return self.__vacancies

# if __name__ == '__main__':
#     hh_api = HeadHunterAPI()
#     hh_vacancies = hh_api.get_vacancies('python')
#     print(hh_vacancies)

