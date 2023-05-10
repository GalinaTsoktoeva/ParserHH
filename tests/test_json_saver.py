import json


def test_get_vacancies_by_salary(some_JSONSaver):
    res = some_JSONSaver.get_vacancies_by_salary("40000-150000")
    assert len(res) == 2

def test_delete_vacancy(some_JSONSaver, some_Vacancy):

    path_file="../src/vacancies.json"

    with open(path_file, "r", encoding='utf-8') as file:
        data1 = json.load(file)

    some_JSONSaver.delete_vacancy(some_Vacancy)

    with open(path_file, "r", encoding='utf-8') as file:
        data2 = json.load(file)
    assert len(data1) == len(data2)+1

def test_add_vacancy(some_JSONSaver, some_Vacancy):

    path_file = "../src/vacancies.json"

    with open(path_file, "r", encoding='utf-8') as file:
        data1 = json.load(file)

    some_JSONSaver.add_vacancy(some_Vacancy)

    with open(path_file, "r", encoding='utf-8') as file:
        data2 = json.load(file)
    assert len(data1) == len(data2) - 1
