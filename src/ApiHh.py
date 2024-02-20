import requests
import json
from start_pack.AbstractApi import AbstractApi


class ApiHh(AbstractApi):
    def get_vacancy(self, search_query, link_hh):
        keys = {'text': f'NAME:{search_query}', 'area': 113, 'per_page': 100}
        vacancy = requests.get(link_hh, keys)
        try:
            return json.loads(vacancy.text)['items']
        except KeyError:
            print(f'Увы, но запрос ({search_query}) не прошел... Возможно неполадки на сервере(')
            return None
