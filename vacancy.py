class Vacancy:
    def __init__(self, title, salary, description, url):
        self.title = title
        self.salary = salary
        self.description = description
        self.url = url

    def __repr__(self) -> str:
        return (f'\n\nВакансия: {self.title}\n'
                f'Зарплата: {self.salary}\n'
                f'Требования: {self.description}\n'
                f'Ссылка: {self.url}')

    @staticmethod
    def vacancy_filter(vacancy: dict) -> dict:
        """Проверка зарплаты(указана, не указана) и """
        filtered_vacancy = {'title': vacancy['name'],
                            'salary': vacancy['salary'],
                            'description': vacancy['snippet']['requirement'],
                            'url': vacancy['url']}
        if filtered_vacancy['salary'] is None:
            filtered_vacancy['salary'] = 'Не указана'
        else:
            sal_from = filtered_vacancy['salary']['from']
            sal_to = filtered_vacancy['salary']['to']
            currency = filtered_vacancy['salary']['currency']
            if sal_to is None:
                filtered_vacancy['salary'] = f'{sal_from} {currency}'
            elif sal_from is None:
                filtered_vacancy['salary'] = f'{sal_to} {currency}'
            else:
                filtered_vacancy['salary'] = f'{sal_from} - {sal_to} {currency}'
        return filtered_vacancy

