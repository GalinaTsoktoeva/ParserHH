from src.api import HeadHunterAPI, SuperJobAPI
from src.vacancy import Vacancy
from src.json_saver import JSONSaver


def sort_vacancies(filtered_vacancies):
    return sorted(filtered_vacancies, key=lambda filter: filter['name'])

def get_top_vacancies(sorted_vacancies, top_n):
    return sorted_vacancies[:top_n]

def main():
    # Use a breakpoint in the code line below to debug your script.
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    word_for_search = input('Введите вакансию для поиска: ').strip()

    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()

    # Получение вакансий с разных платформ
    hh_vacancies = hh_api.get_vacancies(vacancy=word_for_search, path_file="../src/vacancies.json")

    superjob_vacancies = superjob_api.get_vacancies(vacancy=word_for_search)


    # Создание экземпляра класса для работы с вакансиями
    vacancy = Vacancy(name="Python Developer", url="<https://hh.ru/vacancy/123456>", area="Москва", salary_from=100_000,
                      salary_to=150_000, employer='Яндекс',
                      requirements='Экспертные знания в техническом стеке: Backend Python')
    new_vacancy_dict = vacancy.dict_vacancy()

    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver()
    json_saver.add_vacancy(new_vacancy_dict)
    json_saver.get_vacancies_by_salary("100_000-150_000")
    json_saver.delete_vacancy(new_vacancy_dict)

    # Функция для взаимодействия с пользователем
    def user_interaction():
        platforms = ["HeadHunter", "SuperJob"]
        #search_query = input("Введите поисковый запрос: ")
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
        filtered_vacancies = vacancy.filter_vacancies(filter_words)
        #print(filtered_vacancies)

        if not filtered_vacancies:
            print("Нет вакансий, соответствующих заданным критериям.")
            return
        sorted_vacancies = sort_vacancies(filtered_vacancies)
        top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
        print(*top_vacancies, sep="\n")
    user_interaction()



if __name__ == '__main__':
    main()
