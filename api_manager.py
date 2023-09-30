from abc import ABC, abstractmethod
from vacancy import Vacancy
from config import SJ_KEY

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
        'salary': { 'salary_from': ... , 'salary_to: ...},
        'description': 'описание'
        'url': ...
        }"""
        pass


class HHAPIManager(APIManager):
    """Класс для работы с API HeadHunter"""

    def __init__(self, keyword):
        self.keyword = keyword
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {"text": keyword}

    def get_vacancies(self) -> list:
        """Получает вакансии по заданному keyword и возвращает список экземпляра класса Vacancy"""
        response = requests.get(url=self.url, params=self.params).json()
        return self.format_data(response)

    def format_data(self, data) -> list:
        """Форматирует получение по API данные к единому формату:
        {'name' : 'вакансия',
        'salary': { 'salary_from': ... , 'salary_to: ...},
        'description': 'описание'
        'url': ...
        }"""
        vacancies = []
        for vacancy in data['items']:
            filtered_vacancy = {'title': vacancy['name'],
                                'salary': vacancy['salary'],
                                'description': vacancy['snippet']['requirement'],
                                'url': vacancy['url']}
            vac = Vacancy(**filtered_vacancy)
            vacancies.append(vac)
        return vacancies


class SJAPIManager(APIManager):
    """Класс для работы с API SuperJob"""

    def __init__(self, keyword):
        self.keyword = keyword
        self.params = {
            'keyword': self.keyword,
            'page': 0,
            'count': 20
        }
        self.url = 'https://api.superjob.ru/2.0/vacancies/'
        self.headers = {'X-Api-App-Id': SJ_KEY}

    def get_vacancies(self):
        """Получает вакансии по заданному keyword и возвращает список экземпляра класса Vacancy"""
        response = requests.get(self.url, headers=self.headers, params=self.params).json()
        return self.format_data(response)

    def format_data(self, data) -> list:
        """Форматирует получение по API данные к единому формату:
        {'name' : 'вакансия',
        'salary': { 'salary_from': ... , 'salary_to: ...},
        'description': 'описание'
        'url': ...
        }"""
        vacancies = []
        for vacancy in data['objects']:
            formated_vacancy = {'title': vacancy['profession'],
                                'salary': {
                                    'from': vacancy['payment_from'],
                                    'to': vacancy['payment_to']
                                },
                                'description': vacancy['candidat'],
                                'url': vacancy['link']}
            vac = Vacancy(**formated_vacancy)
            vacancies.append(vac)
        return vacancies
