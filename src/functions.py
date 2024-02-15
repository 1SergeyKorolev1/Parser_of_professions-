from heapq import nlargest

from src.Vacancy import Vacancy


def get_top_n(query_top_n, start_pack):
    vacancy_list = start_pack.data_json.get_data(start_pack.vacancy_path)
    list_vacancy = []
    for vacancy in vacancy_list:
        if vacancy['salary'] != None:
            list_vacancy.append(Vacancy(vacancy))
    res = nlargest(query_top_n, list_vacancy, key=lambda vacancy: vacancy.salary_vacancy)
    return res
