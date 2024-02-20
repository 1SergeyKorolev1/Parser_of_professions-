
def app_operation(start_pack):
    search_query = input("Введите название вакансии для поиска: ")
    vacancy = start_pack.api.get_vacancy(search_query)
    start_pack.data_json.add_data(vacancy, start_pack.vacancy_path)

    query_top_n = int(input("Введите количество вакансий для вывода в топ N по зарплате: "))
    top_n, list_vacancy = start_pack.vacancy_instance.get_top_n(query_top_n, start_pack)
    for i in top_n:
        print(f'\n{i}')

    filter_words = input("\nВведите ключевые слова для фильтрации вакансий через пробел: ").split(' ')
    top_filter_words = start_pack.vacancy_instance.get_filter_vacancy(filter_words, list_vacancy)
    for i_ in top_filter_words:
        print(f'\n{i_}')


