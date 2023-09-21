from abc import ABC, abstractmethod


class APIManager(ABC):
    """Класс для работы с API"""

    @abstractmethod
    def get_vacancies(self, keyword):
        """Получает вакансии по заданному keyword"""
        pass

    @abstractmethod
    def format_data(self):
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

    def get_vacancies(self, keyword):
        """Получает вакансии по заданному keyword"""
        pass

    def format_data(self):
        """Форматирует получение по API данные к единому формату:
        {'name' : 'вакансия',
        'salary_min': ...
        'salary_max': ...
        'description': 'описание'
        ...
        }"""
        pass


class SJAPIManager(APIManager):
    """Класс для работы с API SuperJob"""
    def get_vacancies(self, keyword):
        """Получает вакансии по заданному keyword"""
        pass

    def format_data(self):
        """Форматирует получение по API данные к единому формату:
        {'name' : 'вакансия',
        'salary_min': ...
        'salary_max': ...
        'description': 'описание'
        ...
        }"""
        pass
