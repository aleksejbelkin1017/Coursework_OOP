from typing import Any, Union


class Vacancy:
    """Класс для представления вакансии с основными атрибутами: id, название, компания, зарплата, ссылка"""
    __slots__ = ('id', '_name', '_company', '_salary', '_url')

    def __init__(self, id: int, name: str, company: str, salary: Union[int, float], url: str):
        """Инициализация объекта Vacancy с валидацией входных данных.
            :param id: Уникальный идентификатор вакансии
            :param name: Название вакансии
            :param company: Название компании-работодателя
            :param salary: Зарплата
            :param url: Ссылка на вакансию
        """
        self.id = id
        self._name = self.__validate_name(name)
        self._company = self.__validate_company(company)
        self._salary = self.__validate_salary(salary)
        self._url = self.__validate_url(url)

    @property
    def name(self) -> str:
        """Возвращает название вакансии"""
        return self._name

    @property
    def company(self) -> str:
        """Возвращает название компании-работодателя"""
        return self._company

    @property
    def salary(self) -> Union[int, float]:
        """Возвращает зарплату"""
        return self._salary

    @property
    def url(self) -> str:
        """Возвращает ссылку на вакансию"""
        return self._url

    def __validate_name(self, name: str) -> str:
        """
        Метод для валидации названия вакансии.

        :param name: Название вакансии
        :return: Валидное название вакансии или сообщение об ошибке
        """
        if not isinstance(name, str) or not name:
            return "Название вакансии не указано"
        return name

    def __validate_company(self, company: str) -> str:
        """
        Метод для валидации работодателя.

        :param company: Название компании-работодателя
        :return: Валидное название компании или сообщение об ошибке
        """
        if not isinstance(company, str) or not company:
            return "Название компании-работодателя не указано"
        return company

    def __validate_salary(self, salary: Union[int, float]) -> Union[int, float]:
        """
        Метод для валидации суммы заработной платы.

        :param salary: Зарплата
        :return: Валидная зарплата или 0 в случае ошибки
        """
        if not isinstance(salary, (int, float)) or salary < 0:
            return 0
        return salary

    def __validate_url(self, url: str) -> str:
        """
        Метод для валидации ссылки на вакансию.

        :param url: Ссылка на вакансию
        :return: Валидная ссылка или сообщение об ошибке
        """
        if not isinstance(url, str) or not url.startswith("http"):
            return "Ссылка не указана"
        return url

    def __lt__(self, other: 'Vacancy') -> bool:
        """Сравнение вакансий по зарплате (меньше)"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary < other.salary

    def __le__(self, other: 'Vacancy') -> bool:
        """Сравнение вакансий по зарплате (меньше или равно)"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary <= other.salary

    def __eq__(self, other: Any) -> bool:
        """Сравнение вакансий по зарплате (равно)"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary == other.salary

    def __ne__(self, other: Any) -> bool:
        """Сравнение вакансий по зарплате (не равно)"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary != other.salary

    def __gt__(self, other: 'Vacancy') -> bool:
        """Сравнение вакансий по зарплате (больше)"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary > other.salary

    def __ge__(self, other: 'Vacancy') -> bool:
        """Сравнение вакансий по зарплате (больше или равно)"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary >= other.salary

    def __repr__(self) -> str:
        """Строковое представление объекта Vacancy"""
        return f"Vacancy(name='{self.name}', company='{self.company}', salary={self.salary}, url='{self.url}')"

    def to_dict(self) -> dict:
        """Преобразование объекта Vacancy в словарь"""
        return {
            'id': self.id,
            'name': self.name,
            'company': self.company,
            'salary': self.salary,
            'url': self.url
        }
