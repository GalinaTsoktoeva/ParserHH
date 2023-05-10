import pytest
from src.api import HeadHunterAPI
from src.api import SuperJobAPI
from src.json_saver import JSONSaver
from src.vacancy import Vacancy

@pytest.fixture()
def some_HeadHunterAPI():
    return HeadHunterAPI()

@pytest.fixture()
def some_SuperJobAPI():
    return SuperJobAPI()

@pytest.fixture()
def some_JSONSaver():
    return JSONSaver()

@pytest.fixture
def some_Vacancy():
    vacancy = Vacancy(name="Python Developer", url="<https://hh.ru/vacancy/123456>", area="Москва", salary_from=100_000, salary_to=150_000, employer='Яндекс', requirements='Экспертные знания в техническом стеке: Backend Python')
    new_vacancy_dict = vacancy.dict_vacancy()
    return new_vacancy_dict


