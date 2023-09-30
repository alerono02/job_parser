class Vacancy:
    def __init__(self, title, salary, description, url):
        self.title = title
        self.salary = self.get_salary(salary)
        self.description = description
        self.url = url

    def __repr__(self) -> str:
        return (f'\n\nВакансия: {self.title}\n'
                f'Зарплата: {self.format_salary()}\n'
                f'Требования: {self.description}\n'
                f'Ссылка: {self.url}')

    def __lt__(self, other):
        """
        :param other: сравнение заработной платы
        :return: True or False
        """
        return (self.salary['from'], self.salary['to']) < (other.salary['from'], other.salary['to'])

    def __gt__(self, other):
        """
        :param other: сравнение заработной платы
        :return: True or False
        """
        return (self.salary['from'], self.salary['to']) > (other.salary['from'], other.salary['to'])

    @staticmethod
    def get_salary(salary):
        """
        :param salary:
        :return: словарь salary {'from': ... , 'to': ...}
        """
        if salary is None:
            salary = {
                'from': 0,
                'to': 0
            }
            return salary
        else:
            salary_from = salary['from']
            salary_to = salary['to']
            if salary_to is None:
                return {'to': 0, 'from': salary_from}
            elif salary_from is None:
                return {'to': salary_to, 'from': 0}
            else:
                return salary

    def format_salary(self):
        """
        :return: Формат вывода зарплаты
        """
        return f'{self.salary["from"]} - {self.salary["to"]}'
