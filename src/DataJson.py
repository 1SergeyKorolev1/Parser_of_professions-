import json
from start_pack.AbstractData import AbstractData


class DataJson(AbstractData):
    def get_data(self, vacancy_path):
        with open(vacancy_path, encoding='utf-8') as f:
            return json.load(f)

    def add_data(self, vacancy, vacancy_path):
        with open(vacancy_path, 'w', encoding='utf-8') as f:
            # f.write(json.dumps(vacancy, ensure_ascii=False))
            json.dump(vacancy, f, ensure_ascii=False)

    def delete_data(self, vacancy_path):
        with open(vacancy_path, 'w', encoding='utf-8') as f:
            v = ''
            json.dump(v, f, ensure_ascii=False)
