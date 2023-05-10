import json


def test_init_HHAPI(some_HeadHunterAPI):
    assert some_HeadHunterAPI.url == 'https://api.hh.ru/vacancies'
    assert some_HeadHunterAPI.area == 1
    path_file = "../src/vacancies.json"

    with open(path_file, "r", encoding='utf-8') as file:
        data1 = json.load(file)

    some_HeadHunterAPI.get_vacancies(vacancy="Python", path_file="../src/vacancies.json")

    with open(path_file, "r", encoding='utf-8') as file:
        data2 = json.load(file)
    assert len(data1) + 3 == len(data2)


def test_init_SuperJob(some_SuperJobAPI):
    assert some_SuperJobAPI.url == 'https://api.superjob.ru/2.0/%s'


    path_file = "../src/vacancies.json"

    with open(path_file, "r", encoding='utf-8') as file:
        data1 = json.load(file)

    some_SuperJobAPI.get_vacancies(vacancy="Python")

    with open(path_file, "r", encoding='utf-8') as file:
        data2 = json.load(file)
    assert len(data1) + 3 == len(data2)

