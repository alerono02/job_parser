from abc import ABC, abstractmethod
from vacancy import Vacancy

import requests


class APIManager(ABC):
    """Класс для работы с API"""

    @abstractmethod
    def get_vacancies(self):
        """Получает вакансии по заданному keyword"""
        pass

    @abstractmethod
    def format_data(self, data):
        """Форматирует получение по API данные к единому формату:
        {'name' : 'вакансия',
        'salary_min': ...
        'salary_max': ...
        'description': 'описание'
        ...
        }"""
        pass


class HHAPIManager(APIManager):
    """Класс для работы с API HeadHunter"""

    def __init__(self, keyword):
        self.keyword = keyword
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {"text": keyword}

    def get_vacancies(self) -> list:
        """Получает вакансии по заданному keyword"""
        response = requests.get(url=self.url, params=self.params).json()
        return self.format_data(response)

    def format_data(self, data) -> list:
        """Форматирует получение по API данные к единому формату:
        {'name' : 'вакансия',
        'salary_from': ...
        'salary_to': ...
        'description': 'описание'
        ...
        }"""
        vacancies = []
        for vacancy in data['items']:
            vac = Vacancy(**Vacancy.vacancy_filter(vacancy))
            vacancies.append(vac)
        return vacancies


class SJAPIManager(APIManager):
    """Класс для работы с API SuperJob"""

    def get_vacancies(self):
        """Получает вакансии по заданному keyword"""
        pass

    def format_data(self, data):
        """Форматирует получение по API данные к единому формату:
        {'name' : 'вакансия',
        'salary_min': ...
        'salary_max': ...
        'description': 'описание'
        ...
        }"""
        pass
