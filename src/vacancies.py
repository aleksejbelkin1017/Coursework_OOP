class Vacancy:
    __slots__ = ('id', '_name', '_company', '_salary', '_url')

    def __init__(self, id, name, company, salary, url):
        self.id = id
        self._name = self.__validate_name(name)
        self._company = self.__validate_company(company)
        self._salary = self.__validate_salary(salary)
        self._url = self.__validate_url(url)

    @property
    def name(self):
        return self._name

    @property
    def company(self):
        return self._company

    @property
    def salary(self):
        return self._salary

    @property
    def url(self):
        return self._url

    def __validate_name(self, name):
        """Метод для валидации названия вакансии"""
        if not isinstance(name, str) or not name:
            return "Название вакансии не указано"
        return name

    def __validate_company(self, company):
        """Метод для валидации работодателя"""
        if not isinstance(company, str) or not company:
            return "Название компании-работодателя не указано"
        return company

    def __validate_salary(self, salary):
        """Метод для валидации суммы заработной платы"""
        if not isinstance(salary, (int, float)) or salary < 0:
            return 0
        return salary

    def __validate_url(self, url):
        """Метод для валидации ссылки на вакансию"""
        if not isinstance(url, str) or not url.startswith("http"):
            return "Ссылка не указана"
        return url

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary < other.salary

    def __le__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary <= other.salary

    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary == other.salary

    def __ne__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary != other.salary

    def __gt__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary > other.salary

    def __ge__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary >= other.salary

    def __repr__(self):
        return f"Vacancy(name='{self.name}', company='{self.company}', salary={self.salary}, url='{self.url}')"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'company': self.company,
            'salary': self.salary,
            'url': self.url
        }
