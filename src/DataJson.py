import json
from src.AbstractData import AbstractData


class DataJson(AbstractData):
    def get_data(self):
        pass

    def add_data(self, vacancy, vacancy_path):
        print(vacancy)
        with open(vacancy_path, 'w', encoding='utf-8') as f:
            # f.write(json.dumps(vacancy, ensure_ascii=False))
            json.dump(vacancy, f, ensure_ascii=False)


    def delete_data(self):
        pass
