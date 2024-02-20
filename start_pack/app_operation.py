
def app_operation(start_pack):
    while True:
        search_query = input("Введите название вакансии для поиска: ")
        vacancy = start_pack.api.get_vacancy(search_query, start_pack.link_hh)
        if vacancy:
            start_pack.data_json.add_data(vacancy, start_pack.vacancy_path)
            while True:
                query_top_n = input("Введите количество вакансий для вывода в топ N по зарплате: ")
                if query_top_n == '':
                    query_top_n = '0'
                if query_top_n.isdigit():
                    top_n, list_vacancy = start_pack.vacancy_instance.get_top_n(int(query_top_n), start_pack)
                    for i in top_n:
                        print(f'\n{i}')
                    break
                else:
                    print('\nОставьте поле пустым - либо введите число, а не строку!..')

            filter_words = input("\nВведите ключевые слова для фильтрации вакансий через пробел: ").split(' ')
            top_filter_words = start_pack.vacancy_instance.get_filter_vacancy(filter_words, list_vacancy)
            for i_ in top_filter_words:
                print(f'\n{i_}')

            start_pack.data_json.delete_data(start_pack.vacancy_path)
            res = input('\nесли хотите выйти - не чего не вводите. Чтоб начать заново введите что ни будь\n')
            if res == '':
                break
        else:
            break


