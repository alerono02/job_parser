from api_manager import HHAPIManager, SJAPIManager
from vacancy import Vacancy
from file_manager import JSONFileManager
import json


def user_interaction():
    """
    Функция для взаимодействия с пользователем
    :return: None
    """
    while True:
        print('Выберите платформу для поиска')
        user_input = input('1 - HeadHunter\n'
                           '2 - SuperJob\n'
                           '3 - HeadHunter и SuperJob\n'
                           '4 - Выход из программы\n')

        if user_input in ('1', '2', '3', '4'):

            if user_input == '1':
                """Работа с вакансиями с HH"""
                keyword = input('Введите вакансию: ')
                hh = HHAPIManager(keyword)
                hh_vacs = hh.get_vacancies()
                not_empty(hh_vacs)

            elif user_input == '2':
                """Работа с вакансиями с SJ"""
                keyword = input('Введите вакансию: ')
                sj = SJAPIManager(keyword)
                sj_vacs = sj.get_vacancies()
                not_empty(sj_vacs)

            elif user_input == '3':
                """Работа с вакансиями с HH и SJ"""
                keyword = input('Введите вакансию: ')
                hh_for_all = HHAPIManager(keyword)
                sj_for_all = SJAPIManager(keyword)
                all_vacs = hh_for_all.get_vacancies() + sj_for_all.get_vacancies()
                not_empty(all_vacs)

            elif user_input == '4':
                break
        else:
            print('Некорректный ввод. Введите число')


def vacancies_interaction(file_manage: JSONFileManager):
    """
    Функция для работы с вакансиями (вывод, требуемая заработная плата, сортировка по зп)
    :param file_manage: экземпляр класса для работы с файлом
    :return:
    """
    while True:
        vacancies = file_manage.read()
        print('\nВыберите опцию: ')
        user_input_for_vacs = input('1 - Вывод вакансий\n'
                                    '2 - Выбор вакансий по заработной плате\n'
                                    '3 - Вернуться\n'
                                    '4 - Выход из программы\n')

        if user_input_for_vacs in ('1', '2', '3', '4', '5'):

            if user_input_for_vacs == '1':
                for vac in vacancies:
                    print(Vacancy(**vac))

            elif user_input_for_vacs == '2':
                salary_input_min = int(input('Введите желаемую минимальную заработную плату: '))
                salary_input_max = int(input('Введите желаемую минимальную заработную плату: '))
                requirement_salary = {'salary': {'from': salary_input_min,
                                                 'to': salary_input_max}}
                requirement_salary_list = file_manage.get_vacancies_by_keyword(requirement_salary)

                while True:
                    sort_input = input('\nКак отсортировать заработную плату?\n'
                                       '1 - По возрастанию\n'
                                       '2 - По убыванию\n'
                                       '3 - Вернуться\n')

                    if sort_input in ('1', '2', '3'):

                        if sort_input == '1':
                            sorted_vacs = equal(format_to_class(requirement_salary_list))
                            print(sorted_vacs)
                            print("\nОтсортировано!\n")
                            break

                        elif sort_input == '2':
                            sorted_vacs = reverse_equal(format_to_class(requirement_salary_list))
                            print(sorted_vacs)
                            print("\nОтсортировано!\n")
                            break

                        elif sort_input == '3':
                            break

            elif user_input_for_vacs == '3':
                break

            elif user_input_for_vacs == '4':
                exit()
        else:
            print('Некорректный ввод. Введите число')


def equal(vacancies: list[Vacancy]):
    """Сравнение зп по возрастанию"""
    return sorted(vacancies)


def reverse_equal(vacancies: list[Vacancy]):
    """Сравнение зп по убыванию"""
    return sorted(vacancies, reverse=True)


def format_to_class(vacancies: dict):
    formate_vacs = []
    for vac in vacancies:
        formate_vacs.append(Vacancy(**vac))
    return formate_vacs


def not_empty(data):
    """
    Проверяет на наличие вакансий
    :param data: полученный список вакансий
    :return:
    """
    if data:
        file_manage = JSONFileManager()
        file_manage.write(data)
        file_manage.read()
        vacancies_interaction(file_manage)
    else:
        print("\nНекорректный ввод, повторите запрос\n")
