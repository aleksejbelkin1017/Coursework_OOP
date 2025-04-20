import json

from src.head_hunter_api import HeadHunterAPI, BaseHeadHunterAPI
from abc import abstractmethod
import requests
from requests.exceptions import HTTPError, RequestException

hh_api = HeadHunterAPI()
user_input_keyword = input('Введите ключевое слово для вакансии: ')
hh_vacancies = hh_api.get_vacancies(user_input_keyword)

with open('data/vacancies_1.json', 'w', encoding='utf-8') as outfile:
    json.dump(hh_vacancies, outfile, ensure_ascii=False, indent=4)

# params = {"text": "python"}
# vacancies = requests.get("https://api.hh.ru/vacancies", params=params).json()
#
# print(vacancies["items"])