import pathlib
from start_pack.app_operation import app_operation

from src.DataJson import DataJson
from src.ApiHh import ApiHh

api = ApiHh()
data_json = DataJson()

project_path = pathlib.Path(__file__).parent.parent
vacancy_path = pathlib.Path(project_path, 'data', 'vacancy.json')

