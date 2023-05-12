from abc import ABC, abstractmethod
from src.vacancy import Vacancy
import requests
import json
from src.json_saver import JSONSaver
import os
import time


class Api(ABC):

    @abstractmethod
    def get_vacancies(self, vacancy):
        pass


class HeadHunterAPI(Api):

    def __init__(self):
        self.name = "Head hunter"
        self.area = 1
        self.url = 'https://api.hh.ru/vacancies'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}')"

    def __str__(self):
        return f"{self.name}"

    def get_vacancies(self, page=0, vacancy="", path_file=None):
        """Парсинг 500 вакансий c сайта"""
        for page_no in range(5):
            params = {
                'text': vacancy,  # Текст фильтра. В имени должно быть слово "Python"
                'area': self.area,  # Поиск оcуществляется по вакансиям города Москва
                'page': page_no,  # Индекс страницы поиска на HH
                'per_page': '100' # Кол-во вакансий на 1 странице
            }

            req = self.get_json_from_hh(params)  # Посылаем запрос к API
            parsed = json.loads(req.content)

            req.close()
        #print(parsed)
            if parsed.get('items'):
                for item in parsed.get('items'):

                    if item:
                #print(item)
                        new_vacancy = Vacancy(
                            name=item['name'],
                            url=item['alternate_url'],
                            area=item["area"]['name'],
                            salary_to=item['salary']['to'] if item['salary'] is not None else 0,
                            salary_from=item['salary']['from'] if item['salary'] is not None else 0,
                            requirements=item['snippet']['requirement'],
                            employer=item['employer']['name']
                        )
                        new_json = JSONSaver()
                        new_vacancy_dict = new_vacancy.dict_vacancy()
                        new_json.add_vacancy(new_vacancy_dict)


    def get_json_from_hh(self, params):
        try:
            response = requests.get(self.url, params)
            return response
        except ConnectionError:
            print('Connection error!')
        except requests.HTTPError:
            print('HTTP error')
        except TimeoutError:
            print('Timeout error')
        return {}


class SuperJobAPI(Api):

    API_KEY = {'X-Api-App-Id': 'v3.r.137520007.f71b02f5cfcb8af64b3f1969216b1a76fe3487b1.3532a9602ded47ada0729bbffe85cf4cdb51ad16'}

    def __init__(self):
        self.name = "Super JOB"
        self.url = 'https://api.superjob.ru/2.0/%s'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}')"

    def __str__(self):
        return f"{self.name}"

    def get_vacancies(self, vacancy):
        """Парсинг 500 вакансий  сайта"""
        vacancies_list = []
        for page_no in range(5):
            params = {'town': 'Москва', # Поиск оcуществляется по вакансиям города Москва
                  'keywords': vacancy, # Текст фильтра. В имени должно быть слово "Python"
                  'catalogues': [56, 52, 51, 48, 47, 604, 42, 41, 40, 546, 503, 37, 36], #поиск по вакансиям разработчиков
                  'page': page_no,
                  'count': 100} # Кол-во вакансий на 1 странице

            request = self.generate_request_for_vacancies_by_parameters(params)
            vacancies = self.get_json_from_superjob(request, SuperJobAPI.API_KEY)
            #print(vacancies)
            for item in vacancies['objects']:
                if item:
                    #print(item)
                    new_vacancy = Vacancy(
                        name=item['profession'],
                        url=item['link'],
                        area=item['town']['title'],
                        salary_to=item['payment_to'] if item['payment_to'] is not None else 0,
                        salary_from=item['payment_from'] if item['payment_from'] is not None else 0,
                        requirements=item['vacancyRichText'],
                        employer=item['firm_name']
                    )
                    new_json = JSONSaver()
                    new_vacancy_dict = new_vacancy.dict_vacancy()
                    new_json.add_vacancy(new_vacancy_dict)
                    vacancies_list.append(new_vacancy_dict)
        #print(vacancies_list)
        return vacancies_list

    def get_json_from_superjob(self, request, auth_data):
        try:
            response = requests.get(self.url % request, headers=auth_data)
            return response.json()
        except ConnectionError:
            print('Connection error!')
        except requests.HTTPError:
            print('HTTP error')
        except TimeoutError:
            print('Timeout error')
        return {}

    def generate_request_for_vacancies_by_parameters(self, parameters):
        result = 'vacancies/?'
        arrays = {'ids', 'keywords', 'm', 't', 'o', 'c', 'driving_licence', 'catalogues'}
        for key in parameters:
            if key not in arrays:
                result += '%s=%s&' % (key, parameters[key])
            elif key == 'catalogues':
                result += 'catalogues='
                for catalogue in parameters[key]:
                    result += '%d,' % catalogue
                result += '%s&' % result[:-1]
            elif key == 'driving_licence':
                for num_of_category, category in enumerate(parameters[key]):
                    result += 'driving_licence[%d]=%s&' % (num_of_category, category)
            elif key == 'keyword':
                for num_of_keyword, keyword in enumerate(parameters[key]):
                    result += '%s[%d][%s]&' % (key, num_of_keyword, keyword)
        return result[:-1]


