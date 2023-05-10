import json
import os
from pathlib import Path

class JSONSaver():
    """Класс для сохранение информации о вакансиях в файл"""
    path_file = "../src/vacancies.json"

    def __init__(self):
        pass

    def add_vacancy(self, vacancy):
        """Функция для добавления вакансии в файл"""
        try:
            with open(JSONSaver.path_file, 'r', encoding='utf-8') as f:

                if os.path.getsize(JSONSaver.path_file) == 0:
                    data = []
                else:
                    data = json.load(f)

            for item in data:
                if item.get('url') == vacancy.get('url'):
                    return

            with open(JSONSaver.path_file, 'w', encoding="utf-8") as file:
                data.append(vacancy)
                json.dump(data, file, ensure_ascii=False, indent='\t', separators=(', ', ': '))

        except FileNotFoundError:
            print(f"Не найден файл + {JSONSaver.path_file}")

    def get_vacancies_by_salary(self, salary):
        """Функция для фильтрации вакансий по зарплате"""
        path = Path(JSONSaver.path_file)
        salary_vac_from = 0
        salary_vac_to = 0
        res = []
        salary_from, salary_to = salary.split('-')
        try:
            with open(JSONSaver.path_file, 'r', encoding="utf-8") as file:
                vacancies = json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            print(f"Не найден файл + {JSONSaver.path_file}")

        for item in vacancies:

            if item.get('salary_from') is None:
                salary_vac_from = 0
            else:
                salary_vac_from = item.get('salary_from')

            if item.get('salary_to') is None:
                salary_vac_to = salary_vac_from
            else:
                salary_vac_to = item.get('salary_to')

            if int(salary_vac_from) >= int(salary_from) and (int(salary_vac_to) <= int(salary_to)):
                res.append(item)

        return res

    def delete_vacancy(self, vacancy):
        """Функция для удаления вакансии из файла"""
        path = Path(JSONSaver.path_file)

        try:
            with open(JSONSaver.path_file, 'r', encoding="utf-8") as file:
                vacancies = json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            print(f"Не найден файл + {JSONSaver.path_file}")

        delete_list = []
        for num, item in enumerate(vacancies):
            if vacancy.get('name') == item.get('name') and vacancy.get('requirements') == item.get('requirements'):
                delete_list.append(num)

        revert_list = delete_list[::-1]
        for num in revert_list:
            del vacancies[num]

        try:
            with open(JSONSaver.path_file, 'w', encoding="utf-8") as file:
                json.dump(vacancies, file, ensure_ascii=False, indent='\t', separators=(', ', ': '))
        except FileNotFoundError:
            print(f"Не найден файл + {JSONSaver.path_file}")

