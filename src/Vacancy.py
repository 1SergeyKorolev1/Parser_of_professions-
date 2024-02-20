from heapq import nlargest


class Vacancy:
    def __init__(self, vacancy: dict = None):
        try:
            self.__vacancy = vacancy
            self.name_vacancy = vacancy['name']
            self.link_vacancy = vacancy['apply_alternate_url']
        except TypeError:
            self.__vacancy = None
            self.name_vacancy = None
            self.link_vacancy = None

    def __str__(self):
        return (f'Имя: {self.name_vacancy}\n'
                f'Зарплата: {self.salary_vacancy}\n'
                f'Описание: {self.description}\n'
                f'Ссылка: {self.link_vacancy}\n')

    @staticmethod
    def get_top_n(query_top_n, start_pack):
        vacancy_list = start_pack.data_json.get_data(start_pack.vacancy_path)
        list_vacancy = []
        for vacancy in vacancy_list:
            if vacancy['salary']:
                list_vacancy.append(Vacancy(vacancy))
        res = nlargest(query_top_n, list_vacancy, key=lambda x: x.salary_vacancy)
        return res, list_vacancy

    @staticmethod
    def get_filter_vacancy(filter_words: list, list_vacancy: list):
        filter_list = []
        for i in list_vacancy:
            for i_ in filter_words:
                if i_.lower() in i.description.lower():
                    filter_list.append(i)
        return filter_list

    @property
    def salary_vacancy(self):
        """"""
        if self.__vacancy['salary']['from']:
            salary = self.__vacancy['salary']['from']
            return salary
        else:
            salary = self.__vacancy['salary']['to']
            return salary

    @property
    def description(self):
        """"""
        if self.__vacancy['snippet']['requirement']:
            res = self.__vacancy['snippet']['requirement']
        else:
            res = ''
        if self.__vacancy['snippet']['responsibility']:
            res_ = self.__vacancy['snippet']['responsibility']
        else:
            res_ = ''
        return res + res_
