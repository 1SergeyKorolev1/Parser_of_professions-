import requests
import json
from src.AbstractApi import AbstractApi


class ApiHh(AbstractApi):
    def get_vacancy(self, search_query):
        keys_response = {'text': f'NAME:{search_query}', 'area': 113, 'per_page': 100, }
        vacancy = requests.get(f'https://api.hh.ru/vacancies', keys_response)
        return json.loads(vacancy.text)['items']
