
def app_operation(start_pack):
    search_query = input("Введите поисковый запрос: ")

    vacancy = start_pack.api.get_vacancy(search_query)
    start_pack.data_json.add_data(vacancy, start_pack.vacancy_path)
