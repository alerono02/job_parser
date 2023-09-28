from abc import ABC, abstractmethod
from config import FILENAME

import json


class FileManager(ABC):
    """Класс для работы с файлами"""

    @abstractmethod
    def read(self):
        """Считывает файл"""
        pass

    @abstractmethod
    def write(self, data):
        """Записывает в файл"""
        pass

    @abstractmethod
    def delete(self, vacancies):
        """Удаление вакансии"""
        pass


class JSONFileManager(FileManager):
    """Класс для работы с JSON файлами"""

    def __init__(self):
        self.filename = FILENAME + '.json'

    def read(self):
        with open(self.filename, 'r') as file:
            print(file.read())

    def write(self, data):
        """Записывает в файл"""
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(json.dumps(data))
        return f'Файл {self.filename} создан!'

    def delete(self, vacancies):
        """Удаление вакансии"""
        pass
