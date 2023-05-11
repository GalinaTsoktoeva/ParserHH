import json


class Vacancy():
    """Класс для создание экземпляра класса для работы с вакансиями"""
    def __init__(self, name, url, area, salary_from, salary_to, requirements, employer):
        self.name = name
        self.url = url
        self.area = area
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.requirements = requirements
        self.employer = employer

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.url}, {self.employer})"

    def __str__(self):
        return f"{self.name}"

    def dict_vacancy(self):
        vacancy = {}
        vacancy['name'] = self.name
        vacancy['url'] = self.url
        vacancy['area'] = self.area
        vacancy['salary_from'] = self.salary_from
        vacancy['salary_to'] = self.salary_to
        vacancy['requirements'] = self.requirements
        vacancy['employer'] = self.employer

        return vacancy

    @staticmethod
    def filter_vacancies(filter_words):
        """Функция для фильтрации вакансий по ключевым словам"""
        result = []
        path_file = "../src/vacancies.json"
        try:
            with open(path_file, "r", encoding='utf-8') as file:
                vacancies = json.load(file)
        except FileNotFoundError:
            print(f"Не найден файл + {path_file}")
            return {}

        for word in filter_words:
            for item in vacancies:
                if word.lower() in item.get("name").lower():
                        #or word.lower() in item.get("requirements").lower():
                    result.append(item)

        return result

