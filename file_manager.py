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
    def write(self):
        """Записывает в файл"""
        pass


class JSONFileManager(FileManager):
    """Класс для работы с JSON файлами"""

    def __init__(self):
        self.filename = FILENAME + '.json'

    def read(self):
        """Считывает файл"""
        pass

    def write(self):
        """Записывает в файл"""
        pass
