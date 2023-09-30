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
        with open(self.filename, 'r', encoding='utf-8') as file:
            data = file.read()
        json_reform_data = json.loads(data)
        return json_reform_data

    def write(self, vacancies):
        """Записывает в файл"""
        data = self.data_to_json(vacancies)
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write(json.dumps(data, ensure_ascii=False, indent=4))
        print(f'\nДанные записаны в {self.filename} \n')

    @staticmethod
    def data_to_json(vacancies):
        vacancies_list = []
        for vacancy in vacancies:
            vacancy_dict = {'title': vacancy.title,
                            'url': vacancy.url,
                            'salary': vacancy.salary,
                            'description': vacancy.description
                            }
            vacancies_list.append(vacancy_dict)
        return vacancies_list

    def delete(self, vacancies):
        """Удаление вакансии"""
        with open(self.filename, 'r', encoding='utf-8') as file:
            data_to_delete = file.read()
        data = json.loads(data_to_delete)
        for vac in data:
            if vac not in vacancies:
                data.remove(vac)
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write(json.dumps(data, ensure_ascii=False, indent=4))
        print("Неподходящие вакансии удалены")

    def get_vacancies_by_keyword(self, keyword: dict):
        with open(self.filename, 'r', encoding='utf-8') as file:
            data = file.read()
        data = json.loads(data)
        filtered_vacancies = []
        for vacancy in data:
            indicator = True
            for key, value in keyword.items():
                if key == 'salary':
                    for k, v in keyword[key].items():
                        if k == 'from':
                            if vacancy['salary']['from'] < v:
                                indicator = False
                        elif k == 'to':
                            if vacancy['salary']['to'] < v:
                                indicator = False

                    if indicator:
                        filtered_vacancies.append(vacancy)
        return filtered_vacancies
