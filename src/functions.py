from heapq import nlargest
from src.Vacancy import Vacancy


def get_top_n(query_top_n, start_pack):
    vacancy_list = start_pack.data_json.get_data(start_pack.vacancy_path)
    list_salary = []
    for vacancy in vacancy_list:
        if vacancy['salary'] != None:
            list_salary.append(Vacancy(vacancy))
    res = nlargest(query_top_n, list_salary, key=lambda x: x.salary_vacancy)
    for i in res:
        print(f'\n{i}')
